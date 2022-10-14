from django.contrib import admin
from django.urls import path
from vpcsc import views

urlpatterns = [
    path("",views.index,name='home'),

    path("about_1",views.about_1,name='about_1'),
    path("about_2",views.about_2,name='about_2'),
    path("about_3",views.about_3,name='about_3'),

    path("contact",views.contact,name='contact'),

    path("bcs",views.bcs,name='bcs'),
    path("bca",views.bca,name='bca'),
    path("bba",views.bba,name='bba'), 

    path("photo",views.photo,name='photo'),
    path("video",views.video,name='video'), 

     path("facilities",views.facilities,name='facilities'), 

    


    path("eligibility",views.eligibility,name='eligibility'),
    path("required_documents",views.required_documents,name='required_documents'),

    

    path("placement",views.placement,name='placement'),

    path("sports",views.sports,name='sports'),
    path("nss",views.nss,name='nss'),
    path("library",views.library,name='library'),
    path("syllabi",views.syllabi,name='syllabi'),
    path("exami",views.exami,name='exami'),
    path("results",views.results,name='results'),
    path("scholarships",views.scholarships,name='scholarships'),
    path("student_helpline",views.student_helpline,name='student_helpline'),

   

]
