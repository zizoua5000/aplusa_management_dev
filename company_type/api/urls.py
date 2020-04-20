from django.urls import path
from company_type.api.views import CompanyTypeListCreateAPIView,CompanyTypeUpdateDeleteAPIView

app_name='company_type'
urlpatterns = [
    path('list_create/', CompanyTypeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', CompanyTypeUpdateDeleteAPIView.as_view(),name='update_delete')
]
