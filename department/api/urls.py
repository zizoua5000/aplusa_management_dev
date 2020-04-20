from django.urls import path
from department.api.views import DepartmentListCreateAPIView,DepartmentUpdateDeleteAPIView

app_name='department'
urlpatterns = [
    path('list_create/', DepartmentListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', DepartmentUpdateDeleteAPIView.as_view(),name='update_delete')
]
