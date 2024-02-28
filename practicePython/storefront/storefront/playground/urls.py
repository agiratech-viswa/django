from django.urls import path, include
from . import views

# from storefront.views import say    # taken view from project file

#URLConf
urlpatterns = [
    path('',views.say_hello),  # path('hello/',views.say_hello)
]