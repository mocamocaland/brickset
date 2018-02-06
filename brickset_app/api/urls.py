from django.conf.urls import url
from api import views


urlpatterns = [
    url(r"^items/$", views.item_list, name="item_list"),
    url(r"^items/(?P<item_id>\d+)$", views.item_detail, name="item_detail"),
]