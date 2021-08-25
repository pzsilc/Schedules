from .models import Drugstore, Schedule, UserProfile
from .serializers import DrugstoreSerializer, DrugstoreDetailSerializer, ScheduleSerializer, UserDetailSerializer
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import DrugstorePermission
from django.shortcuts import render
import os
# Create your views here.



class Home:
	def index(request, pk=None):
		return render(request, 'index.html')



class UserDetailsView(generics.RetrieveAPIView):
	serializer_class = UserDetailSerializer
	permission_classes = (IsAuthenticated,)

	def get_object(self):
		return self.request.user



class DrugstoreAPIView(generics.ListCreateAPIView):
	serializer_class = DrugstoreSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Drugstore.objects.all()
		serializer = UserDetailSerializer(instance=self.request.user)
		data = serializer.data
		return [Drugstore.objects.get(pk=drugstore) for drugstore in list(data['profile']['drugstores'])]



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