from rest_framework import serializers
from .models import Drugstore, Schedule, UserDrugstoreRelation
from django.contrib.auth.models import User
import base64
import os



class DrugstoreDetailSerializer(serializers.ModelSerializer):
	schedules = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Drugstore
		fields = ['pk', 'name','schedules',]

	def to_representation(self, value):
		data = super().to_representation(value)
		for index, pk in enumerate(data['schedules']):
			data['schedules'][index] = ScheduleSerializer(Schedule.objects.get(pk=pk)).data
			with open(os.path.dirname(os.path.abspath(__file__)) + '/..' + data['schedules'][index]['file'], 'rb') as file:
				data['schedules'][index]['file'] = base64.b64encode(file.read())
		return data



class DrugstoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Drugstore
		fields = ['pk', 'name',]



class ScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = ['pk', 'name', 'file', 'created_at', 'drugstore',]



class UserDetailSerializer(serializers.ModelSerializer):
	drugstore = serializers.SerializerMethodField('get_drugstore')

	def get_drugstore(self, obj):
		if obj.is_superuser:
			return '__all__'
		else:
			try:
				rel = UserDrugstoreRelation.objects.get(user=obj)
				return rel.drugstore.pk
			except:
				return None

	class Meta:
		model = User
		fields = ['pk', 'email', 'is_superuser', 'drugstore']