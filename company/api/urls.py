from django.urls import path
from company.api.views import CompanyListCreateAPIView,CompanyUpdateDeleteAPIView

app_name='company'
urlpatterns = [
    path('list_create/', CompanyListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', CompanyUpdateDeleteAPIView.as_view(),name='update_delete')
]
