from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Employees

def Index(request):
    employee_list = Employees.objects.all().order_by('id')  # You can change ordering
    paginator = Paginator(employee_list, 4)  # Show 5 employees per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})

def Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES.get("image")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = Employees(
            name = name,
            image = image,
            email = email,
            address = address,
            phone = phone,
        )
        emp.save()
    return redirect('home')

def Update(request,id):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES.get("image")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = Employees(
            id = id,
            name = name,
            image = image,
            email = email,
            address = address,
            phone = phone,
        )

        emp.save()
    return redirect('home')

def Delete(request,id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    # context = {
    #     'empDel' : emp,
    # }
    

    return redirect('home')

def DeleteAll(request):
    pass
# def DeleteAll(request):
#     if request.method == 'POST':
#         emp_ids = request.POST.getlist('id[]')

#         for emp_id in emp_ids:
#             try:
#                 emp = Employees.objects.get(pk=int(emp_id))  # ✅ Use emp_id
#                 emp.delete()
#             except Employees.DoesNotExist:
#                 pass

#         return JsonResponse({'status': 'deleted'})
#     return JsonResponse({'status': 'invalid method'}, status=405)

