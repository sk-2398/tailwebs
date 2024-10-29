from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        marks = request.POST['marks']

        # Checking and updating if student with same subject already exist 
        student, created = Student.objects.update_or_create(
            name=name,
            subject=subject,
            defaults={'marks': marks}
        )

        if created:
            messages.success(request, "New student added successfully.")
        else:
            messages.success(request, "Existing student record updated successfully.")

        return redirect('student_list')  

    return render(request, 'student_list.html')  

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.subject = request.POST['subject']
        student.marks = request.POST['marks']
        student.save()
        messages.success(request, "Student updated successfully.")
        return redirect('student_list')  
    
    return render(request, 'student_list.html', {'students': Student.objects.all(), 'editing_student': student})
    
@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, "Student deleted successfully.")
    return redirect('student_list')
