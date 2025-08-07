from django.contrib import admin
from django.urls import path
from  app import views

urlpatterns = [
    path('',views.index, name='index'),
    path('donor_register',views.donor_register, name='donor_register'),
    path('donor_log_in',views.donor_log_in, name= 'donor_log_in'),
    path('donor_dashboard',views.donor_dashboard, name= 'donor_dashboard'),
    path('buyer_register',views.buyer_register, name= 'buyer_register'),
    path('buyer_log_in',views.buyer_log_in, name= 'buyer_log_in'),
    path('buyer_dashboard',views.buyer_dashboard, name= 'buyer_dashboard'),
    path('hospital_register',views.hospital_register, name= 'hospital_register'),
    path('hospital_log_in',views.hospital_log_in, name= 'hospital_log_in'),
    path('hospital_dashboard',views.hospital_dashboard, name= 'hospital_dashboard'),
    path('donor_list',views.donor_list, name= 'donor_list'),
    path('buyer_list',views.buyer_list, name= 'buyer_list'),
    path('form',views.form, name= 'form'),
    path('form1',views.form1, name= 'form1'),
    path('documents/<str:email>/', views.documents, name='documents'),
    path('document1/<str:email>/', views.document1, name='document1'),
    path('application', views.application, name='application'),
    path('application1', views.application1, name='application1'),
    path('log_out',views.log_out, name= 'log_out'),
    path('donor',views.donor, name= 'donor'),
    path('buyer',views.buyer, name= 'buyer'),
    path('before_opt/<str:email>/',views.before_opt, name= 'before_opt'),
    path('after_opt/<str:email>/',views.after_opt, name= 'after_opt'),
    path('view_doc/<str:email>/',views.view_doc, name= 'view_doc'),
    path('view_document/<str:email>/',views.view_document, name= 'view_document')
]

