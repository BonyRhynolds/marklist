from .import views
from django.urls import path

urlpatterns = [
    path("",views.home,name="home"),
    path("form",views.form,name="forms"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('detail/<int:id>/',views.detail,name="detail"),
]

