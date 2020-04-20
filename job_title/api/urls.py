from django.urls import path
from job_title.api.views import JobTitleListCreateAPIView,JobTitleUpdateDeleteAPIView

app_name='job_title'
urlpatterns = [
    path('list_create/', JobTitleListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', JobTitleUpdateDeleteAPIView.as_view(),name='update_delete')
]
