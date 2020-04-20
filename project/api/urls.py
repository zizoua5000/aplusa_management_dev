from django.urls import path
from project.api.views import ProjectListCreateAPIView,ProjectUpdateDeleteAPIView

app_name='project'
urlpatterns = [
    path('list_create/', ProjectListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>',ProjectUpdateDeleteAPIView.as_view(),name='update_delete')
]
