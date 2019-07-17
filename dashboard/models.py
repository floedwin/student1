from __future__ import unicode_literals
from django.db import models
#from django.db.models import
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Study_material(models.Model):
    book_id = models.IntegerField('book_id',unique=True,db_index=True)
    subject = models.CharField('subject',max_length=200, default='')
    book_name = models.CharField('book_name',max_length=100,default='')
    serial_number= models.IntegerField('serial_number',default='')
    author = models.CharField('author',max_length=100)


    def __str__(self):
        return self.book_name

class Homework( models.Model):
    student_id = models.IntegerField('student_id',unique=True, db_index=True)
    student_name =models.CharField('student_name', max_length=200, default='')
    year = models.CharField('class', max_length=100, default='')
    subject = models.CharField('subject', max_length=100, default='')
    homework_date = models.DateTimeField('homework_date', default=timezone.now)
    submission_date = models.DateTimeField('submission_date', default=timezone.now)
    status = models.CharField('status', max_length=100, default='')
    action = models.CharField('action', max_length=100, default='')

    def __str__(self):
        return self.student_name


class Syllabus(models.Model):
    subject = models.CharField('subject',max_length=30, unique=True)
    description = models.CharField('description',max_length=100)
    topic=models.CharField('topic',max_length=100)
    study_material = models.ForeignKey(Study_material, related_name='syllabus',on_delete=models.CASCADE)

    def __str__(self):
        return self.subject



class Post(models.Model):
    message = models.TextField(max_length=4000)
    homework = models.ForeignKey(Homework, related_name='posts',on_delete=models.CASCADE)
    study_material = models.ForeignKey(Study_material,related_name='posts',on_delete=models.CASCADE)
    year = models.CharField('class', max_length=100, default='')
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.CASCADE)


class Upload_assignment(models.Model):
    assignment_id = models.IntegerField('assignment_id', unique=True, db_index=True)
    subject = models.CharField('subject',max_length=100,unique=True)
    assignment_name = models.CharField('assignment_name',max_length=100,unique=True)
    year = models.CharField('class', max_length=100, default='')
    teacher_name = models.CharField('teacher_name', max_length=100, unique=True)
    upload_at = models.DateTimeField(null=True)


class Myaccount(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description =models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
   # image = models.ImageField(upload_to='profile_image',blank=True)

    def __str__(self):
        return self.user.username