from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from .models import Plan, Subscription
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from datetime import timedelta
# Create your views here.



# Display Plans View

def plans_view(request):

    plans = Plan.objects.all()

    return render(request, "plans/plans.html", {"plans":plans})



# Add Plan View

def add_plan_view(request):

    if request.method == "POST":
        plan_name = request.POST.get("plan_name")
        plan_feture_1 = request.POST.get("plan_feture_1")
        plan_feture_2 = request.POST.get ("plan_feture_2")
        plan_feture_3 = request.POST.get("plan_feture_3")
        plan_amount = request.POST.get("plan_amount")

        #validation
        if not all([plan_name, plan_feture_1, plan_feture_2, plan_feture_3, plan_amount]):
            messages.error(request, "All fields are required!")
            return render(request, "plans/add_plan.html")
        
        try:
            
            plan_amount = int(plan_amount)

            new_plan = Plan(
                plan_name=plan_name,
                plan_feture_1=plan_feture_1,
                plan_feture_2=plan_feture_2,
                plan_feture_3=plan_feture_3,
                plan_amount=plan_amount,
            )
            new_plan.save()

            messages.success(request, "Plan added successfully!", "alert-success")
            return redirect("plans:plans_view")
        
        
        except ValueError:
            messages.error(request, "Plan amount must be a valid number.", "alert-danger")
            return render(request, "plans/add_plan.html")

    return render(request, "plans/add_plan.html")





#Detail Plan View

def plan_detail_view(request, plan_id):

    plan = get_object_or_404(Plan, id=plan_id)

    return render(request, "plans/plan_detail.html", {"plan": plan})





#Update Plane View

def update_plan_view(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)  

    if request.method == "POST":
        plan.plan_name = request.POST.get("plan_name", plan.plan_name)
        plan.plan_feture_1 = request.POST.get("plan_feture_1", plan.plan_feture_1)
        plan.plan_feture_2 = request.POST.get("plan_feture_2", plan.plan_feture_2)
        plan.plan_feture_3 = request.POST.get("plan_feture_3", plan.plan_feture_3)
        plan.plan_amount = request.POST.get("plan_amount", plan.plan_amount)

        plan.save() 
        messages.success(request, "Plan updated successfully!", "alert-success")
        return redirect("plans:plan_detail_view", plan_id=plan.id)  

    return render(request, "plans/update_plan.html", {"plan": plan})







#Delete Plane View

def delete_plan_view(request, plan_id):

    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        plan.delete()

        messages.success(request, 'Plan deleted successfully.', 'alert-danger')
        return redirect("plans:plans_view")
      
    else:
        return render(request, 'plans/plan_detail.html', {'plan': plan})






#Payment View

def payment_view(request, plan_id):
    
    plan = get_object_or_404(Plan, id=plan_id)
    

    return render(request, "plans/payment.html", {"plan": plan})





#Payment Result View

def payment_result_view(request, plan_id):

    plan = get_object_or_404(Plan, id=plan_id)
    payment_status = request.GET.get("status") 
    payment_status = request.GET.get("status")  
    transaction_id = request.GET.get("id")      
    amount = request.GET.get("amount")          
    message = request.GET.get("message") 
    
    #For debugging
    print(f"Payment Status: {payment_status}")
    print(f"Transaction ID: {transaction_id}")
    print(f"Amount: {amount}")
    print(f"Message: {message}")


    if payment_status == "paid":
        subscription, created = Subscription.objects.get_or_create(
            user=request.user,
            defaults={"plan": plan, "is_active": True, "start_date": now(), "end_date": now() + timedelta(days=30)}
        )

        if not created:
            subscription.plan = plan
            subscription.is_active = True
            subscription.start_date = now()
            subscription.end_date = now() + timedelta(days=30)
            subscription.save()
            
        
        
        context = {
            "plan": plan,
            "transaction_id": transaction_id,
            "amount": amount,
            "message": message,
            "subscription": subscription
        }
        
        return render(request, "plans/payment_success.html", context)


    


    elif payment_status in ["failed", "denial"]:
        context = {
            "plan": plan,
            "transaction_id": transaction_id,
            "amount": amount,
            "message": message
        }
        return render(request, "plans/payment_failed.html", context)
    

    else:
        context = {"plan": plan, "message": "Unknown payment status."}

        return render(request, "plans/payment_failed.html", context)
