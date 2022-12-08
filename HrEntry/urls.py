from django.urls import path
from .import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("AboutPage",views.AboutPage,name='AboutPage'),
    path("Contact",views.Contact,name="Contact"),
    path("AllJobs",views.AllJobs,name="AllJobs"),
    path("Services",views.Services,name="Services"),
    
    path('JobView/<int:pk>',views.JobView,name='JobView'),
    path('AdminHome',views.AdminHome,name="AdminHome"),
    path("AdminJobList",views.AdminJobList,name='AdminJobList'),
    
    path('Signin',views.Signin,name='Signin'),
    path('Signout',views.Signout,name="Signout"),
    
    path('AddJob',views.AddJob,name='AddJob'),
    path("AdminJobApplicationList",views.AdminJobApplicationList,name="AdminJobApplicationList"),
    path("AdminJobView/<int:pk>",views.AdminJobView,name='AdminJobView'),
    path("UpdateJob/<int:pk>",views.UpdateJob,name='UpdateJob'),
    path("DeleteJob/<int:pk>",views.DeleteJob,name='DeleteJob'),
    path("ApplyJob",views.ApplyJob,name="ApplyJob"),
    path("EMessage",views.EMessage,name="EMessage"),
    
    path("ApplicantView/<int:pk>",views.ApplicantView,name="ApplicantView"),
    path("DeleteApplicant/<int:pk>",views.DeleteApplicant,name="DeleteApplicant"),
    path("RegApplicantView/<int:pk>",views.RegApplicantView,name="RegApplicantView"),
    path("DeleteDropApplicant/<int:pk>",views.DeleteDropApplicant,name="DeleteDropApplicant"),
    
    path('EmployersMessageView',views.EmployersMessageView,name='EmployersMessageView'),
    path('EmployerMsgIndi/<int:pk>',views.EmployerMsgIndi,name="EmployerMsgIndi"),
    path("DeleteEployersMsg/<int:pk>",views.DeleteEployersMsg,name="DeleteEployersMsg"),
    
    
]
