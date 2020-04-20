#BU HELELIKDIR
from rest_framework.permissions import BasePermission
class CustomDjangoModelPermissions(BasePermission):
    message="Ale duz yazda"
    def has_object_permission(self,request,view, obj):
        return True

#Sonradan bunu geri qaytar . ESAS BUDUE
# from rest_framework.permissions import (DjangoModelPermissions)
# class CustomDjangoModelPermissions(DjangoModelPermissions):

#     #This is for database permissions
#     def __init__(self):
#         self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
 