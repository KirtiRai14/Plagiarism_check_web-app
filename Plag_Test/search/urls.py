from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('',views.display,name='display'),
    path('',views.accept,name='accept'),
    path('',views.reject,name='reject'),
    path('',views.change_the_question,name='change_the_question'),
]