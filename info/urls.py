from django.urls import path
from . import views
app_name='info'

urlpatterns = [
    path('',views.home,name='home'),
    path('contact-me/',views.contact ,name='contact' )
]
