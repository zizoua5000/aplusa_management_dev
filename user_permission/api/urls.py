from django.urls import path
# from user_permission.api.views import UserPermissionListAPIView,UserPermissionCreateAPIView,UserPermissionDeleteAPIView,UserPermissionDetailAPIView
from user_permission.api.views import UserPermissionListAPIView,UserPermissionCreateAPIView,UserPermissionDetailAPIView

app_name='user_permission'
urlpatterns = [
    path('list/', UserPermissionListAPIView.as_view(),name='list'),
    path('detail/<pk>', UserPermissionDetailAPIView.as_view(),name='detail'),
    path('create/', UserPermissionCreateAPIView.as_view(),name='create'),
    # path('delete/<user>/<permission>/', UserPermissionDeleteAPIView.as_view(),name='delete')
]
