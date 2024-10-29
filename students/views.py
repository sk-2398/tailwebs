from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from teachers.models import Teacher  # Make sure to import the Teacher model

@login_required
def student_list(request):
    # Get the teacher associated with the logged-in user
    print(request.user.id)
    teacher = get_object_or_404(Teacher, user=request.user)
    # Filter students to show only those created by the logged-in teacher
    try:
        students = Student.objects.filter(teacher=teacher)
    except:
        students=[]
    return render(request, 'student_list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        marks = request.POST['marks']

        # Get the logged-in teacher
        teacher = get_object_or_404(Teacher, user=request.user)

        # Checking and updating if a student with the same subject already exists
        student, created = Student.objects.update_or_create(
            name=name,
            subject=subject,
            teacher=teacher,  # Associate the student with the logged-in teacher
            defaults={'marks': marks}
        )

        if created:
            messages.success(request, "New student added successfully.")
        else:
            messages.success(request, "Existing student record updated successfully.")

        return redirect('student_list')

    return render(request, 'add_student.html')  # Change the template if needed

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    # Ensure the logged-in teacher is the one who created this student
    if student.teacher.user != request.user:
        messages.error(request, "You do not have permission to edit this student.")
        return redirect('student_list')

    if request.method == 'POST':
        student.name = request.POST['name']
        student.subject = request.POST['subject']
        student.marks = request.POST['marks']
        student.save()
        messages.success(request, "Student updated successfully.")
        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})  # Change template to edit_student.html

@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    # Ensure the logged-in teacher is the one who created this student
    if student.teacher.user != request.user:
        messages.error(request, "You do not have permission to delete this student.")
        return redirect('student_list')

    student.delete()
    messages.success(request, "Student deleted successfully.")
    return redirect('student_list')
