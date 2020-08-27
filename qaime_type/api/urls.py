from django.urls import path
from qaime_type.api.views import QaimeTypeListCreateAPIView,QaimeTypeUpdateDeleteAPIView

app_name='qaime_type'
urlpatterns = [
    path('list_create/', QaimeTypeListCreateAPIView.as_view(),name='list_create'),
    path('update_delete/<pk>', QaimeTypeUpdateDeleteAPIView.as_view(),name='update_delete')
]
