from rest_framework import permissions
from .models import UserProfile


class DrugstorePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        #check if user wants to destroy
        return not (request.method == 'DELETE' and not request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        profile = UserProfile.objects.get(user=request.user)
        return obj.pk in [d.pk for d in profile.drugstores.all()]

