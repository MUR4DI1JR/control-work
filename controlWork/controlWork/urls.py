from django.contrib import admin
from django.urls import path
from realEstate.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', registration_page, name='registration_page'),
    path('login', login_page, name='login_page'),
    path('', real_estate_list),
    path('<slug:slug>/', detailsRealEstate, name="detailsRealEstate")
]
