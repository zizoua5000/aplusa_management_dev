from django.urls import path
from content_type.api.views import ContentTypeListCreateAPIView,ContentTypeUpdateDeleteAPIView

app_name='content_type'
urlpatterns = [
    path('list_create/',ContentTypeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', ContentTypeUpdateDeleteAPIView.as_view(),name='update_delete')
]
