from django.conf.urls import url
from api import views


urlpatterns = [
    url("^items/$", views.item_list, name="item_list"),
    
]