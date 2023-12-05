
from django.urls import path, include
from .views import (
    index,
    create_blog,
    update_blog,
    delete_blog,
    area_show,
    update_area,
    delete_area,

)
urlpatterns = [
    path('', index),
    path('create/', create_blog),
    path('update/<int:id>', update_blog),
    path('delete/<int:id>', delete_blog),
    path('area/', area_show),
    path('area_update/<int:id>/', update_area),
    path('area_delete/<int:id>/', delete_area),
]