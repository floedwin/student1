from django.views.generic import TemplateView
from django.shortcuts import render
from dashboard.models import Study_material,Homework,Syllabus,Post,Upload_assignment

# Create your views here.
def home(request):
    return render(request,'home.html')

def about_us(request):
    return render(request,'about_us.html')

def contact(request):
    return  render(request,'contact.html')

def tables_data(request):
    return render(request,'tables_data.html')

def my_account(request):
    return render(request,'my_account.html')

class study_material(TemplateView):
    template_name = 'study_materials.html'
    def get (self,request):
        study_material=Study_material.objects.all()
        args = {'study_material': study_material}
        return render(request, self.template_name, args)

class homework(TemplateView):
    template_name = 'homework.html'
    def get (self,request):
        homework=Homework.objects.all()
        args = {'homework': homework}
        return render(request, self.template_name, args)

class syllabus(TemplateView):
    template_name = 'syllabus.html'
    def get(self,request):
        syllabus=Syllabus.objects.all()
        args = {'syllabus': syllabus}
        return  render(request, self.template_name, args)

class post(TemplateView):
    template_name = 'post.html'
    def get(self,request):
        post=Post.objects.all()
        args = {'post': post}
        return  render(request, self.template_name, args)


class upload_assignment(TemplateView):
    template_name = 'upload_assignment.html'
    def get(self,request):
        upload_assignment=Upload_assignment.objects.all()
        args = {'upload_assignment': upload_assignment}
        return  render(request, self.template_name, args)
