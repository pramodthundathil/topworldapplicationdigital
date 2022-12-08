from django.db import models

# Create your models here.

class JobList(models.Model):
    
    JobID = models.AutoField(primary_key = True)
    PostedDate = models.DateTimeField(auto_now_add=True,editable = False)
    JobTitle = models.CharField(max_length = 255)
    CompanyName= models.CharField(max_length=255)
    Salary = models.CharField(max_length = 255)
    Skills = models.CharField(max_length = 255)
    Qualification = models.CharField(max_length = 255)
    WorkTime = models.CharField(max_length=255)
    Experiance = models.CharField(max_length=255)
    WorkLocation = models.CharField(max_length=255)
    Discription = models.CharField(max_length = 1000)
    
class JobApplication(models.Model):
    
    ApplicationID = models.AutoField(primary_key = True)
    AppliedDate = models.DateTimeField(auto_now_add=True,editable = False)
    Jobid = models.ForeignKey(JobList,on_delete=models.CASCADE,blank=True, null=True)
    JobTitle = models.CharField(max_length = 255)
    FirstName = models.CharField(max_length = 255)
    LastName = models.CharField(max_length = 255)
    PhoneNumber = models.CharField(max_length = 255)
    EmailId = models.CharField(max_length = 255)
    Document = models.FileField(upload_to = 'resumes')
    
class DropedResume(models.Model):
    
    ApplicationID = models.AutoField(primary_key = True)
    AppliedDate = models.DateTimeField(auto_now_add=True,editable = False)
    JobTitle = models.CharField(max_length = 255)
    FirstName = models.CharField(max_length = 255)
    LastName = models.CharField(max_length = 255)
    PhoneNumber = models.CharField(max_length = 255)
    EmailId = models.CharField(max_length = 255)
    Document = models.FileField(upload_to = 'droped_resumes')
    
class EmployersMessage(models.Model):
    
    EmpmassageID = models.AutoField(primary_key=True)
    OrganasationName= models.CharField(max_length=255)
    EmailID = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    Message = models.CharField(max_length=1000)
    
    
    
    
    
    
