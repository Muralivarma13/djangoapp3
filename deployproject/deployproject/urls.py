"""
URL configuration for deployproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basic.views import home,about,contact,sample,sample1,productInfo,filteringData,filterStudentsByCity,pagination,createData,createProduct,createEmployee
from newapp.views import orderPlacing,BookMyshow,GetOrders,BookingDetails,insertbook,getdetails,UpdateAuthor,DeleteBook
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('home/',home),
    path('about/',about),
    path('contact/',contact),
    path('sample/',sample),
    path('sample1/', sample1),
     path('product/', productInfo),
     path('filter/', filteringData),
     path('students/', filterStudentsByCity),
     path('pagination/',pagination),
     path('create/',createData),
     path("productcreate/",createProduct),
     path("emp/",createEmployee),
     path('order/',orderPlacing),
     path("bookticket/",BookMyshow),
     path("getorders/",GetOrders),
     path("getBokings/",BookingDetails),
     path("bookdetails/",insertbook),
     path("getbook/",getdetails),
     path("update-author/", UpdateAuthor),
     path("delete/", DeleteBook)


]
