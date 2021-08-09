from .models import Drugstore, Schedule
from .serializers import DrugstoreSerializer, DrugstoreDetailSerializer, ScheduleSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework import viewsets, generics, mixins
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import DrugstorePermission
import os
# Create your views here.



class UserDetailsView(generics.RetrieveAPIView):
	serializer_class = UserDetailSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return self.request.user



class DrugstoreAPIView(generics.ListCreateAPIView):
	queryset = Drugstore.objects.all()
	serializer_class = DrugstoreSerializer
	permission_classes = (IsAdminUser,)



class DrugstoreDetailAPIView(generics.RetrieveDestroyAPIView):
	queryset = Drugstore.objects.all()
	serializer_class = DrugstoreDetailSerializer
	permission_classes = (IsAuthenticated, DrugstorePermission,)



class ScheduleViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer
	permission_classes = (IsAuthenticated, IsAdminUser,)

	def perform_destroy(self, instance):
		if os.path.isfile(instance.file.path):
			os.remove(instance.file.path)
		instance.delete()