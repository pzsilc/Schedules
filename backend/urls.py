from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from application import views 
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'schedules', views.ScheduleViewSet, basename="ScheduleViewSet")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drugstores/<int:pk>/', views.DrugstoreDetailAPIView.as_view(), name="DrugstoreDetailAPIView"),
    path('api/drugstores/', views.DrugstoreAPIView.as_view(), name="DrugstoreAPIView"),
    path('api/auth/user/', views.UserDetailsView.as_view(), name="UserDetailsView"),
    path('api/auth/', include('rest_auth.urls')),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
