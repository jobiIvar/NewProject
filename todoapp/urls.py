
from django.urls import path

# from . import views
from todoapp import views

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Task_list_view.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.Task_details_view.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Task_update_view.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Task_delete_view.as_view(),name='cbvdelete'),
]
