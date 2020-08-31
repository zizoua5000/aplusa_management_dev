from django.urls import path
from m_project_company.api.views import MProjectCompanyListCreateAPIView,MProjectCompanyUpdateDeleteAPIView

app_name='m_project_company'
urlpatterns = [
    path('list_create/', MProjectCompanyListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', MProjectCompanyUpdateDeleteAPIView.as_view(),name='update_delete')
]
