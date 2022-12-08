from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import JobList,JobApplication,DropedResume,EmployersMessage
# from django.conf import settings

# admin user authentication and logout--------------------------------------

def Signin(request):
    if request.method  == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('AdminHome')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('Signin')
    return render(request,'login.html')

def Signout(request):
    
    logout(request)
    return redirect('Index')


#=======================ADMIN===============================================

# administrator Home screen rendering------------------------------------------

@login_required(login_url="Signin")
def AdminHome(request):
    AllJobs = JobList.objects.all().order_by('-PostedDate').values()
    Applications = JobApplication.objects.all().order_by('-AppliedDate').values()
    DropedResumes = DropedResume.objects.all().order_by('-AppliedDate').values()
    emessage = EmployersMessage.objects.all().order_by('-EmpmassageID').values()
    
    
    context = {
        'Alljobs':AllJobs,
        'NoofJobs':len(AllJobs),
        "applications":Applications,
        "nofappli":len(Applications),
        'noofdropresume':len(DropedResumes),
        "DropedResumes":DropedResumes,
        'noofemployers':len(emessage),
        "emessage":emessage,
        
    }
    return render(request,"admin.html",context)


# Admin Job list handling and new job adding----------------------------------- 

@login_required(login_url="Signin")
def AdminJobList(request):
    
    AllJobs = JobList.objects.all()
    Applications = JobApplication.objects.all()
    
    context = {
        'Alljobs':AllJobs,
        'NoofJobs':len(AllJobs),
        "nofappli":len(Applications),
        
    }
    
    return render(request,'joblist.html',context)

# admin Job Add Function---------------------------------------------------------------

@login_required(login_url="Signin")
def AddJob(request):
    if request.method == 'POST':
        
        JobTitle = request.POST["jtitle"]
        Skills = request.POST["skills"]
        CompanyName = request.POST["company"]
        Salary = request.POST["salary"]
        Discription = request.POST["dis"]
        Qualification = request.POST["qlif"]
        WorkTime = request.POST['workt']
        Experiance = request.POST["experiance"]
        Location = request.POST["location"]
        
        NewJob = JobList.objects.create(JobTitle = JobTitle,CompanyName = CompanyName,Salary = Salary,Skills = Skills,Qualification = Qualification,WorkTime = WorkTime,Experiance=Experiance,WorkLocation=Location,Discription = Discription)
        NewJob.save()
        
        messages.success(request,"New Job Added To the List")
        return redirect("AdminJobList")
        
    return redirect("AdminJobList")

@login_required(login_url="Signin")
def UpdateJob(request,pk):
    myjob = JobList.objects.filter(JobID = pk)
    context = {
        'myjob':myjob
    }
    
    if request.method == "POST":
        
        JobTitle = request.POST["jobtitle"]
        CompanyName = request.POST["company"]
        Salary = request.POST["salary"]
        Skills = request.POST["skills"]
        Qualification = request.POST["qualification"]
        WorkTime = request.POST["worktime"]
        Discription = request.POST["discription"]
        Experiance = request.POST["experiance"]
        Location = request.POST["location"]
        
        myjob = JobList.objects.get(JobID = pk)
        myjob.JobTitle = JobTitle
        myjob.CompanyName = CompanyName
        myjob.Salary = Salary
        myjob.Skills = Skills
        myjob.Qualification = Qualification
        myjob.WorkTime = WorkTime
        myjob.Discription = Discription
        myjob.Experiance = Experiance
        myjob.WorkLocation = Location
        myjob.save()
        messages.info(request,"Job Updated")
        return redirect("AdminJobView",pk = pk)
        
    return render(request,"editjob.html",context)

@login_required(login_url="Signin")
def DeleteJob(request,pk):
    MyJob = JobList.objects.get(JobID = pk)
    MyJob.delete()
    return redirect("AdminHome")

# Jobapplication Handling-------------------------------------------------------------

@login_required(login_url="Signin")
def AdminJobApplicationList(request):
    
    Applications = JobApplication.objects.all().order_by('-AppliedDate').values()
    AllJobs = JobList.objects.all().order_by('-PostedDate').values()
    DropedResumes = DropedResume.objects.all().order_by('-AppliedDate').values()
    
    context = {
        "applications":Applications,
        'NoofJobs':len(AllJobs),
        "nofappli":len(Applications),
        'DropedResumes':DropedResumes,
             
    }
    
    return render(request,"jobapplicationlist.html",context)

@login_required(login_url="Signin")
def AdminJobView(request,pk):
    MyJob = JobList.objects.filter(JobID = pk)
    application = JobApplication.objects.filter(Jobid = pk)
    context = {
        'MyJob':MyJob,
        'applications':application,
        'appicantnum':len(application)
    }
    return render(request,"AdminJobView.html",context)

@login_required(login_url="Signin")
def ApplicantView(request,pk):
    application = JobApplication.objects.filter(ApplicationID = pk)
    
    context = {
        "application":application,
    }
    
    return render(request,"applicantview.html",context)

@login_required(login_url="Signin")
def RegApplicantView(request,pk):
    application = DropedResume.objects.filter(ApplicationID = pk)
    
    context = {
        "application":application,
    }
    
    return render(request,"Dropedapplication.html",context)

@login_required(login_url="Signin")
def DeleteApplicant(request,pk):
    applicant = JobApplication.objects.get(ApplicationID = pk)
    applicant.Document.delete()
    applicant.delete()
    return redirect('AdminHome')

@login_required(login_url="Signin")
def DeleteDropApplicant(request,pk):
    applicant = DropedResume.objects.get(ApplicationID = pk)
    applicant.Document.delete()
    applicant.delete()
    return redirect('AdminHome')

#Employers message Handling----------------------------------------------------------
@login_required(login_url="Signin")
def EmployersMessageView(request):
    emessage = EmployersMessage.objects.all()
    context = {
        "emessage":emessage
    }
    return render(request,"employersmsg.html",context)

@login_required(login_url="Signin")
def EmployerMsgIndi(request,pk):
    emessage = EmployersMessage.objects.filter(EmpmassageID = pk)
    context = {
        "emessage":emessage
    }
    return render(request,"EmployersIndividualMessage.html",context)

@login_required(login_url="Signin")
def DeleteEployersMsg(request,pk):
    applicant = EmployersMessage.objects.get(EmpmassageID = pk)
    applicant.delete()
    return redirect('AdminHome')




#======================================================================================

#User funtions------------------------------------------------------------------------

# index page Rendering---------------------------------------------------------

def Index(request):
    AllJobs = JobList.objects.all().order_by('-PostedDate').values()
    context = {
        'Alljobs':AllJobs
    }
    return render(request,'index.html',context)

def AboutPage(request):
    return render(request,"about.html")

def Contact(request):
    if request.method == "POST":
        messages.info(request,"We appreciate you contacting us. One of our colleagues will get back in touch with you soon! Have a great day!")
        return redirect("Contact")
        
    return render(request,"contact.html")

def Services(request):
    return render(request,"services.html")

def AllJobs(request):
    Alljobs = JobList.objects.all().order_by('-PostedDate').values()
    context = {
        "Alljobs":Alljobs
    }
    return render (request,"alljobs.html",context)

# Job View And Job Application-----------------------------------------------------

def JobView(request,pk):
    
    MyJob = JobList.objects.filter(JobID = pk)
    
    if request.method == "POST":
        
        FirstName = request.POST["fname"]
        LastName = request.POST["lname"]
        JobTitle = request.POST["jobtitle"]
        PhoneNumber = request.POST["phone"]
        EmailId = request.POST["email"]
        Doc = request.FILES['document']
        Jobid = request.POST['jobid']
        
        JobId = JobList.objects.get(JobID = Jobid)
        
        Application = JobApplication.objects.create(Jobid = JobId,JobTitle = JobTitle,FirstName = FirstName,LastName = LastName,PhoneNumber = PhoneNumber,EmailId = EmailId,Document = Doc)
        Application.save()
        
        messages.info(request,"Thank you! Your job application has been sent!")
        return redirect('JobView',pk=Jobid)
        
    return render(request,"jobview.html",{"MyJob":MyJob})

# Resume Drop--------------------------------------------------------------
    
def ApplyJob(request):
    
    if request.method == 'POST':
        
        FirstName = request.POST["fname"]
        LastName = request.POST["lname"]
        JobTitle = request.POST["jobtitle"]
        PhoneNumber = request.POST["phone"]
        EmailId = request.POST["email"]
        Doc = request.FILES['doc']
        
        Application = DropedResume.objects.create(JobTitle = JobTitle,FirstName = FirstName,LastName = LastName,PhoneNumber = PhoneNumber,EmailId = EmailId,Document = Doc)
        Application.save()
        
        messages.success(request," Thank you! Your registration has been successfully completed!")
        return redirect("Index")
    
def EMessage(request):
    
    if request.method == "POST":
        
        Organazation = request.POST["organazation"]
        EmailId = request.POST["email"]
        Phone = request.POST["phone"]
        Message = request.POST["message"]
        
        emessage = EmployersMessage.objects.create(OrganasationName=Organazation,EmailID=EmailId,PhoneNumber=Phone,Message=Message)
        emessage.save()
        messages.success(request,"Thank you for getting in touch, we will respond with in 2 business days")
        return redirect("Index")
        
# def error_404_view(request, exception):
       
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    # return render(request, '404.html')
        




    
