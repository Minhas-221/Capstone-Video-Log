from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('cform',views.MainFormView.as_view()),
    path('form',views.form),
    path('contactus',views.contactus),
]