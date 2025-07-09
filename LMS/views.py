from django.shortcuts import render, HttpResponse, redirect

from .models import Student


def home(request):
    print("Method: ",request.method)
    students = Student.objects.all()
    return render(request, "home.html", {"students":students})


# model_action_view
def student_create_view(request): # http methods Get, Post, Put, Patch, Delete
    if request.method == "POST":
        fullname = request.POST.get("fullname", False)
        age = request.POST.get("age", False)
        email = request.POST.get("email", False)
        bio = request.POST.get("bio", False)
        image = request.FILES.get("image", False)
        if not fullname or not age or not email or not image or not bio:
            return HttpResponse("Error: please fill all datas")
        # student = Student.objects.create(
        #     fullname=fullname,
        #     age=age,
        #     email=email,
        #     bio = bio,
        #     image = image
        # )
        student = Student(
            fullname=fullname,
            age=age,
            email=email,
            bio = bio,
            image = image
        )
        student.save()
        return redirect("home-view")
    elif request.method == "GET":
        return render(request, "student_create.html")
    

def student_detail_view(request, pk):
    student = Student.objects.filter(id=pk).first() # select * from students where id=pk
    if not student:
        return HttpResponse("student doesn't exists")
    return render(request, "student_detail.html", {"data": student})


def student_edit_view(request, pk): # http methods Get, Post, Put, Patch, Delete
    student = Student.objects.filter(id=pk).first()
    if not student:
        return HttpResponse("Student not found")
    if request.method == "POST":
        fullname = request.POST.get("fullname", False)
        age = request.POST.get("age", False)
        email = request.POST.get("email", False)
        bio = request.POST.get("bio", False)
        image = request.FILES.get("image", False)
        if not image:
            image = student.image
        # student = Student.objects.create(
        #     fullname=fullname,
        #     age=age,
        #     email=email,
        #     bio = bio,
        #     image = image
        # )
        student.fullname = fullname
        student.email = email
        student.age = age
        student.bio = bio
        student.image = image
        student.save()
        return redirect("home-view")
    elif request.method == "GET":
        return render(request, "student_create.html", {"student":student})



def student_destroy_view(request, pk):
    student = Student.objects.filter(id=pk).first()
    if not student:
        return HttpResponse("Student not found")
    if request.method =="GET":
        return render(request, "student_delete.html", {"student":student})
    student.delete()
    return redirect("home-view")