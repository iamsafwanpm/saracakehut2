from django.urls import path
from . import views
from .views import bookconsultation_view
from .views import contact_us_view
from .views import about_us_view
from .views import dashboard
from .views import login
from .views import registration_view
from .views import success_page ,contact_success, booking_status




app_name = 'app1'
urlpatterns = [
     path('', views.login, name='login'),
     path('index/',views.index,name="index"),
     path('bookconsultation/', bookconsultation_view, name='bookconsultation'),
     path('/contact_us/', contact_us_view, name='contact_us'),
     path('/about_us.html/', views.about_us_view, name='about_us'),
     path('/client_dashboard/', dashboard, name='dashboard'),
     path('registeration.html',registration_view, name='registeration'),
     path('logout/',views.logout,name='logout'),
     path('success/', success_page, name='success'),
     path('contact_success/', contact_success, name='contact_success'),
     path('booking_status/', booking_status, name='booking_status'),
]