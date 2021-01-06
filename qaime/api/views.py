from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from qaime.api.serializers import QaimeListSerializer,QaimeCreateSerializer,QaimeCreateReturnSerializer,QaimeDetailSerializer,QaimeChangeStatusSerializer
from qaime.api.models import Qaime
from qaime_detail.api.models import QaimeDetail
from device.api.models import Device
from accessory.api.models import Accessory
from accessory_history.api.models import AccessoryHistory
from simcard.api.models import Simcard
from simcard_history.api.models import SimcardHistory
from device_history.api.models import DeviceHistory
from pending.api.models import Pending
from event.api.models import Event
from event_type.api.models import EventType
from action.api.models import Action
from aplusa_management.static_values import *
import collections
from rest_framework.response import Response
from rest_framework import status
from aplusa_management.permissions import CustomDjangoModelPermissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from qaime.api.filters import QaimeFilter
from rest_framework import filters
from django_filters import rest_framework as filter

class QaimeListAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeListSerializer
    filter_class = QaimeFilter
    filter_backends = (filter.DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = '__all__'
    # permission_classes=[IsAuthenticated]

class QaimeDetailAPIView(RetrieveAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeDetailSerializer
    # permission_classes=[IsAuthenticated]

class QaimeCreateAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeCreateSerializer
    # permission_classes=[IsAuthenticated]

class QaimeCreateReturnAPIView(ListCreateAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeCreateReturnSerializer
    # permission_classes=[IsAuthenticated]

class QaimeChangeStatusAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeChangeStatusSerializer
    # permission_classes=[IsAuthenticated]


class QaimeUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    #  This view for deleting Qaime with the type of sell
    #  Method:Delete
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeListSerializer

    def destroy(self, request, *args, **kwargs):
       
        instance = self.get_object()
        print("DELETEDELETEDELETEDELETEDELETE")
        print(instance)
        print("DELETEDELETEDELETEDELETEDELETE")
        if instance.status_id!=STATIC_STATUS_PENDING:
            return Response("NOT DELETED.STATUS OF QAIME COMPLETED !!!",status=status.HTTP_400_BAD_REQUEST)
        if(instance.qaime_type_id==STATIC_QAIME_TYPE_SELLING):
            #This is for selling qaime type
            qaime_details=QaimeDetail.objects.filter(qaime=instance)
            for q_d in qaime_details:
                # q_d.delete()

                # QaimeDetail has 2 types
                #   1.QaimeDetail for devices
                #   2.QaimeDetail for accessories
                if(q_d.device!=None):
                    # 1.QaimeDetail for devices
                    device=q_d.device
                    device_history=DeviceHistory.objects.filter(device=device).order_by('-id').first()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_STATUS_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_LOCATION_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    if(q_d.sold_or_rent==STATIC_SOLD):
                        Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_IS_SOLD_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                        ).last().delete()
                    else:
                        Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_IS_RENT_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                        ).last().delete()
                    
                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_PROJECT_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_COMPANY_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    if(q_d.configuration!=None):
                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_SALES,
                            event_type_id=STATIC_EVENT_TYPE_CONFIGURATION_CHANGED,
                            device_history=device_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()
                    if(q_d.fw_version!=None):
                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_SALES,
                            event_type_id=STATIC_EVENT_TYPE_FW_VERSION_CHANGED,
                            device_history=device_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()
                   
                    device_history.delete()

                    previous_device_history=DeviceHistory.objects.filter(device=device).order_by('-id').first()

                    # If simcard selected we have to handle this situation
                    if(q_d.simcard!=None):
                        simcard=q_d.simcard
                        simcard_history=SimcardHistory.objects.filter(simcard=simcard).order_by('-id').first()
                        
                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_SALES,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_IS_ACTIVE_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()

                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_SALES,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_PLUGGED_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()
                        
                        simcard_history.delete()

                        previous_simcard_history=SimcardHistory.objects.filter(simcard=simcard).order_by('-id').first()
                        if(previous_simcard_history!=None):
                            simcard.is_active=previous_simcard_history.is_active
                            simcard.device=previous_simcard_history.device if previous_simcard_history.device!=None else None
                            simcard.save()
                        else:
                            simcard.is_active=STATIC_SIMCARD_DEACTIVE
                            simcard.device=None
                            simcard.save()
                    

                    if(previous_device_history!=None):
                        device.project=previous_device_history.project if previous_device_history.project!=None else None
                        device.company=previous_device_history.company if previous_device_history.company!=None else None
                        device.simcard=previous_device_history.simcard if previous_device_history.simcard!=None else None
                        device.status=previous_device_history.status if previous_device_history.status!=None else None
                        device.device_event_datetime=previous_device_history.qaime_datetime if previous_device_history.qaime_datetime!=None else None
                        device.recipient=previous_device_history.recipient if previous_device_history.recipient!=None else None
                        device.device_location=previous_device_history.location if previous_device_history.location!=None else None
                        device.configuration=previous_device_history.configuration if previous_device_history.configuration!=None else None
                        device.fw_version=previous_device_history.fw_version if previous_device_history.fw_version!=None else None
                        device.sell_count=previous_device_history.sell_count if previous_device_history.sell_count!=None else None
                        device.is_sold=previous_device_history.is_sold if previous_device_history.is_sold!=None else None
                        device.is_rent=previous_device_history.is_rentbit if previous_device_history.is_rent!=None else None
                        device.save()
                    else:
                        device.project=None
                        device.company=None
                        device.simcard=None
                        device.status_id=STATIC_STATUS_READY_TO_SELL
                        device.device_event_datetime=None
                        device.recipient=None
                        device.device_location_id=STATIC_DEVICE_LOCATION_AT_APLUSA_SECURITY_WAREHOUSE
                        device.configuration=None
                        device.fw_version=None
                        device.sell_count=0
                        device.is_sold=0
                        device.is_rent=0
                        device.save()
                if(q_d.accessory!=None):
                    # 2.QaimeDetail for accessories
                    accessory=q_d.accessory
                    accessory.count=accessory.count+q_d.count
                    accessory.save()

                    last_accessory_history=AccessoryHistory.objects.filter(
                        qaime=instance
                        ).last().delete()
                
                Pending.objects.filter(
                            accessory=q_d.accessory,
                            device=q_d.device,
                            count=q_d.count,
                            recipient=instance.recipient,
                            project=q_d.project,
                            company=q_d.company,
                            status_id=STATIC_STATUS_PENDING
                        ).last().delete()

                Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_SALES,
                        event_type_id=STATIC_EVENT_TYPE_RECIPIENT_CHANGED,
                        qaime=instance,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                q_d.delete()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_200_OK)
        elif(instance.qaime_type_id==STATIC_QAIME_TYPE_RETURN):
            #This is for returning qaime type
            qaime_details=QaimeDetail.objects.filter(qaime=instance)
            for q_d in qaime_details:
                # QaimeDetail has 2 types
                #   1.QaimeDetail for devices
                #   2.QaimeDetail for accessories
                if(q_d.device!=None):
                    # 1.QaimeDetail for devices
                    device=q_d.device
                    device_history=DeviceHistory.objects.filter(device=device).order_by('-id').first()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_STATUS_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_LOCATION_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    if(q_d.sold_or_rent==STATIC_SOLD):
                        Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_IS_SOLD_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                        ).last().delete()
                    else:
                        Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_IS_RENT_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                        ).last().delete()
                    
                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_PROJECT_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_COMPANY_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    # if(q_d.configuration!=None):
                    #     Event.objects.filter(
                    #         action_id=STATIC_ACTION_QAIME_RETURN,
                    #         event_type_id=STATIC_EVENT_TYPE_CONFIGURATION_CHANGED,
                    #         device_history=device_history,
                    #         event_datetime=instance.qaime_datetime
                    #     ).last().delete()
                    # if(q_d.fw_version!=None):
                    #     Event.objects.filter(
                    #         action_id=STATIC_ACTION_QAIME_RETURN,
                    #         event_type_id=STATIC_EVENT_TYPE_FW_VERSION_CHANGED,
                    #         device_history=device_history,
                    #         event_datetime=instance.qaime_datetime
                    #     ).last().delete()
                   
                    device_history.delete()

                    previous_device_history=DeviceHistory.objects.filter(device=device).order_by('-id').first()

                    # If simcard selected we have to handle this situation
                    if(q_d.simcard!=None):
                        simcard=q_d.simcard
                        simcard_history=SimcardHistory.objects.filter(simcard=simcard).order_by('-id').first()
                        
                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_RETURN,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_IS_ACTIVE_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()

                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_RETURN,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_UNPLUGGED_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()
                        
                        simcard_history.delete()

                        previous_simcard_history=SimcardHistory.objects.filter(simcard=simcard).order_by('-id').first()
                        if(previous_simcard_history!=None):
                            simcard.is_active=previous_simcard_history.is_active
                            simcard.device=previous_simcard_history.device if previous_simcard_history.device!=None else None
                            simcard.save()
                        else:
                            simcard.is_active=STATIC_SIMCARD_DEACTIVE
                            simcard.device=None
                            simcard.save()
                    

                    if(previous_device_history!=None):
                        device.project=previous_device_history.project if previous_device_history.project!=None else None
                        device.company=previous_device_history.company if previous_device_history.company!=None else None
                        device.simcard=previous_device_history.simcard if previous_device_history.simcard!=None else None
                        device.status=previous_device_history.status if previous_device_history.status!=None else None
                        device.device_event_datetime=previous_device_history.device_event_datetime if previous_device_history.device_event_datetime!=None else None
                        device.recipient=previous_device_history.recipient if previous_device_history.recipient!=None else None
                        device.device_location=previous_device_history.device_location if previous_device_history.device_location!=None else None
                        device.configuration=previous_device_history.configuration if previous_device_history.configuration!=None else None
                        device.fw_version=previous_device_history.fw_version if previous_device_history.fw_version!=None else None
                        device.sell_count=previous_device_history.sell_count if previous_device_history.sell_count!=None else None
                        device.is_sold=previous_device_history.is_sold if previous_device_history.is_sold!=None else None
                        device.is_rent=previous_device_history.is_rent if previous_device_history.is_rent!=None else None
                        device.save()
                    else:
                        device.project=None
                        device.company=None
                        device.simcard=None
                        device.status_id=STATIC_STATUS_READY_TO_SELL
                        device.device_event_datetime=None
                        device.recipient=None
                        device.device_location_id=STATIC_DEVICE_LOCATION_AT_APLUSA_SECURITY_WAREHOUSE
                        device.configuration=None
                        device.fw_version=None
                        device.sell_count=0
                        device.is_sold=0
                        device.is_rent=0
                        device.save()

                    # There is 2 option:
                    # 1.If previouse case of device was not installed yet, then we have to create Pending data
                    # 2.If previouse case of device was already installed,then we have not change Pending data
                    if(device.status_id==STATIC_STATUS_READY_TO_INSTALL):
                        Pending.objects.create(
                            device=device,
                            project=device.project,
                            company=device.company,
                            count=1,
                            recipient=instance.recipient,
                            status_id=STATIC_STATUS_PENDING
                        )
                if(q_d.accessory!=None):
                    # 2.QaimeDetail for accessories
                    accessory=q_d.accessory
                    accessory.count=accessory.count-q_d.count
                    accessory.save()

                    last_accessory_history=AccessoryHistory.objects.filter(
                        qaime=instance
                        ).last().delete()

                    # There is 2 option:
                    # 1.If accessory not installed yet(if accessory is_new=True) and we decided to delete qaime, then we have to restore Pending data
                    # 2.If accessory already installed(if accessory is_new=False) and we decided to delete qaime,then we have NOT restore Pending data
                    if(accessory.is_new==True):
                        accessory_pending=Pending.objects.filter(
                                accessory=q_d.accessory,
                                project=q_d.project,
                                company=q_d.company,
                                status_id=STATIC_STATUS_PENDING
                            ).last()

                        if(accessory_pending==None):
                            Pending.objects.create(
                                accessory=q_d.accessory,
                                project=q_d.project,
                                company=q_d.company,
                                count=q_d.count,
                                recipient=instance.recipient,
                                status_id=STATIC_STATUS_PENDING
                            )
                        else:
                            accessory_pending.count=accessory_pending.count+q_d.count
                            accessory_pending.save()

                Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_RECIPIENT_CHANGED,
                        qaime=instance,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                q_d.delete()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("SOMETHING WENT WRONG!!!",status=status.HTTP_400_BAD_REQUEST)
    # permission_classes=[IsAuthenticated]


class QaimeUpdateDeleteReturnAPIView(RetrieveUpdateDestroyAPIView):
    #  This view for deleting Qaime with the type of return
    #  Method:Delete
    permission_classes = (CustomDjangoModelPermissions, )
    queryset=Qaime.objects.all()
    serializer_class=QaimeListSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status_id!=STATIC_STATUS_PENDING:
            return Response("NOT DELETED.STATUS OF QAIME COMPLETED !!!",status=status.HTTP_400_BAD_REQUEST)
        if(instance.qaime_type==STATIC_QAIME_TYPE_RETURN):
            #This is for returning qaime type
            qaime_details=QaimeDetail.objects.filter(qaime=instance)
            for q_d in qaime_details:
                # QaimeDetail has 2 types
                #   1.QaimeDetail for devices
                #   2.QaimeDetail for accessories
                if(q_d.device!=None):
                    # 1.QaimeDetail for devices
                    device=q_d.device
                    device_history=DeviceHistory.objects.filter(device=device).order_by('-id').first()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_STATUS_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_DEVICE_LOCATION_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    if(q_d.sold_or_rent==STATIC_SOLD):
                        Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_IS_SOLD_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                        ).last().delete()
                    else:
                        Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_IS_RENT_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                        ).last().delete()
                    
                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_PROJECT_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_COMPANY_CHANGED,
                        device_history=device_history,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                    if(q_d.configuration!=None):
                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_RETURN,
                            event_type_id=STATIC_EVENT_TYPE_CONFIGURATION_CHANGED,
                            device_history=device_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()
                    if(q_d.fw_version!=None):
                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_RETURN,
                            event_type_id=STATIC_EVENT_TYPE_FW_VERSION_CHANGED,
                            device_history=device_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()
                   
                    device_history.delete()

                    previous_device_history=DeviceHistory.objects.filter(device=device).order_by('-id').first()

                    # If simcard selected we have to handle this situation
                    if(q_d.simcard!=None):
                        simcard=q_d.simcard
                        simcard_history=SimcardHistory.objects.filter(simcard=simcard).order_by('-id').first()
                        
                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_RETURN,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_IS_ACTIVE_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()

                        Event.objects.filter(
                            action_id=STATIC_ACTION_QAIME_RETURN,
                            event_type_id=STATIC_EVENT_TYPE_SIMCARD_UNPLUGGED_CHANGED,
                            simcard_history=simcard_history,
                            event_datetime=instance.qaime_datetime
                        ).last().delete()
                        
                        simcard_history.delete()

                        previous_simcard_history=SimcardHistory.objects.filter(simcard=simcard).order_by('-id').first()
                        if(previous_simcard_history!=None):
                            simcard.is_active=previous_simcard_history.is_active
                            simcard.device=previous_simcard_history.device if previous_simcard_history.device!=None else None
                            simcard.save()
                        else:
                            simcard.is_active=STATIC_SIMCARD_DEACTIVE
                            simcard.device=None
                            simcard.save()
                    

                    if(previous_device_history!=None):
                        device.project=previous_device_history.project if previous_device_history.project!=None else None
                        device.company=previous_device_history.company if previous_device_history.company!=None else None
                        device.simcard=previous_device_history.simcard if previous_device_history.simcard!=None else None
                        device.status=previous_device_history.status if previous_device_history.status!=None else None
                        device.device_event_datetime=previous_device_history.device_event_datetime if previous_device_history.device_event_datetime!=None else None
                        device.recipient=previous_device_history.recipient if previous_device_history.recipient!=None else None
                        device.device_location=previous_device_history.device_location if previous_device_history.device_location!=None else None
                        device.configuration=previous_device_history.configuration if previous_device_history.configuration!=None else None
                        device.fw_version=previous_device_history.fw_version if previous_device_history.fw_version!=None else None
                        device.sell_count=previous_device_history.sell_count if previous_device_history.sell_count!=None else None
                        device.is_sold=previous_device_history.is_sold if previous_device_history.is_sold!=None else None
                        device.is_rent=previous_device_history.is_rent if previous_device_history.is_rent!=None else None
                        device.save()
                    else:
                        device.project=None
                        device.company=None
                        device.simcard=None
                        device.status_id=STATIC_STATUS_READY_TO_SELL
                        device.device_event_datetime=None
                        device.recipient=None
                        device.device_location_id=STATIC_DEVICE_LOCATION_AT_APLUSA_SECURITY_WAREHOUSE
                        device.configuration=None
                        device.fw_version=None
                        device.sell_count=0
                        device.is_sold=0
                        device.is_rent=0
                        device.save()

                    # There is 2 option:
                    # 1.If previouse case of device was not installed yet, then we have to create Pending data
                    # 2.If previouse case of device was already installed,then we have not change Pending data
                    if(device.status_id==STATIC_STATUS_READY_TO_INSTALL):
                        Pending.objects.create(
                            device=device,
                            project=device.project,
                            company=device.company,
                            count=1,
                            recipient=instance.recipient,
                            status_id=STATIC_STATUS_PENDING
                        )
                if(q_d.accessory!=None):
                    # 2.QaimeDetail for accessories
                    accessory=q_d.accessory
                    accessory.count=accessory.count-q_d.count
                    accessory.save()

                    # There is 2 option:
                    # 1.If accessory not installed yet(if accessory is_new=True) and we decided to delete qaime, then we have to restore Pending data
                    # 2.If accessory already installed(if accessory is_new=False) and we decided to delete qaime,then we have NOT restore Pending data
                    if(accessory.is_new==True):
                        accessory_pending=Pending.objects.filter(
                                accessory=q_d.accessory,
                                project=q_d.project,
                                company=q_d.company,
                                status_id=STATIC_STATUS_PENDING
                            ).last()

                        if(accessory_pending==None):
                            Pending.objects.create(
                                accessory=q_d.accessory,
                                project=q_d.project,
                                company=q_d.company,
                                count=q_d.count,
                                recipient=instance.recipient,
                                status_id=STATIC_STATUS_PENDING
                            )
                        else:
                            accessory_pending.count=accessory_pending.count+q_d.count
                            accessory_pending.save()

                Event.objects.filter(
                        action_id=STATIC_ACTION_QAIME_RETURN,
                        event_type_id=STATIC_EVENT_TYPE_RECIPIENT_CHANGED,
                        qaime=instance,
                        event_datetime=instance.qaime_datetime
                    ).last().delete()

                q_d.delete()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_200_OK)
    # permission_classes=[IsAuthenticated]