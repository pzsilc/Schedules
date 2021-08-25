from rest_framework import serializers
from .models import Drugstore, Schedule, UserProfile
from django.contrib.auth.models import User
import base64, os




class ScheduleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Schedule
		fields = '__all__'

	def to_representation(self, value):
		data = super().to_representation(value)
		try:
			with open(data['file'], 'rb') as file:
				data['file'] = base64.b64encode(file.read())
		except:
			pass
		return data



class DrugstoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Drugstore
		fields = ('pk', 'name',)



class DrugstoreDetailSerializer(serializers.ModelSerializer):
	schedules = ScheduleSerializer(many=True, read_only=True)
	class Meta:
		model = Drugstore
		fields = '__all__'



class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('drugstores',)



class UserDetailSerializer(serializers.ModelSerializer):
	profile = UserProfileSerializer(required=True)
	class Meta:
		model = User
		fields = ('pk', 'email', 'is_superuser', 'profile')