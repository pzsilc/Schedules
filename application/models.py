from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension
import os
# Create your models here.


class Drugstore(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name


class Schedule(models.Model):
	name = models.CharField(max_length=64)
	file = models.FileField(upload_to='', validators=[validate_file_extension])
	created_at = models.DateTimeField(auto_now=True)
	drugstore = models.ForeignKey(Drugstore, on_delete=models.CASCADE, related_name='schedules')

	def __str__(self):
		return self.name + ' -- ' + self.drugstore.name


class UserDrugstoreRelation(models.Model):
	user = models.ForeignField(User, on_delete=models.CASCADE, blank=True, null=True)
	drugstore = models.ForeignKey(Drugstore, on_delete=models.CASCADE)

	def __str__(self):
		return '#' + str(self.pk)