"""aplusa_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/vehicle_type/', include('vehicle_type.api.urls')),
    path('api/vehicle_mark/', include('vehicle_mark.api.urls')),
    path('api/vehicle_model/', include('vehicle_model.api.urls')),
    path('api/vehicle/', include('vehicle.api.urls')),
    path('api/accessory_model/', include('accessory_model.api.urls')),
    path('api/accessory_type/', include('accessory_type.api.urls')),
    path('api/accessory/', include('accessory.api.urls')),
    path('api/accessory_history/', include('accessory_history.api.urls')),
    path('api/accessory_fixing/', include('accessory_fixing.api.urls')),
    path('api/company_type/', include('company_type.api.urls')),
    path('api/company/', include('company.api.urls')),
    path('api/configuration/', include('configuration.api.urls')),
    path('api/department/', include('department.api.urls')),
    path('api/region/', include('region.api.urls')),
    path('api/simcard/', include('simcard.api.urls')),
    path('api/project/', include('project.api.urls')),
    path('api/price_type/', include('price_type.api.urls')),
    path('api/price/', include('price.api.urls')),
    path('api/job_title/', include('job_title.api.urls')),
    path('api/status/', include('status.api.urls')),
    path('api/person/', include('person.api.urls')),
    path('api/device_type/', include('device_type.api.urls')),
    path('api/device_mark/', include('device_mark.api.urls')),
    path('api/device_model/', include('device_model.api.urls')),
    path('api/device_location/', include('device_location.api.urls')),
    path('api/device_detail/', include('device_detail.api.urls')),
    path('api/device/', include('device.api.urls')),
    path('api/user/', include('user.api.urls')),
    path('api/content_type/', include('content_type.api.urls')),
    path('api/permission/', include('permission.api.urls')),
    path('api/user_permission/', include('user_permission.api.urls')),
    path('api/responsible_person/', include('responsible_person.api.urls')),
    path('api/fw_version/', include('fw_version.api.urls')),
    path('api/action/', include('action.api.urls')),
    path('api/action_group/', include('action_group.api.urls')),
    path('api/event_type/', include('event_type.api.urls')),
    path('api/qaime/', include('qaime.api.urls')),
    path('api/qaime_type/', include('qaime_type.api.urls')),
    path('api/m_project_company/', include('m_project_company.api.urls')),
    path('api/m_vehicle_accessory/', include('m_vehicle_accessory.api.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
