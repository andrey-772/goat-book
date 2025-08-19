from django.urls import path

from lists.tests import home_page

urlpatterns = [
    path("", home_page, name="home")
]
