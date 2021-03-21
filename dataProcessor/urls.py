from django.urls import include, path
from rest_framework import routers

from . import views
from .view_controllers import Storage_facility
from .view_controllers import Grease_and_hydrogen
from .view_controllers import index

app_name = 'dataProcessor'

router = routers.DefaultRouter()
router.register(r'add-seepage', Storage_facility.Storage_facilityViewSet, basename='add-seepage')
router.register(r'add-grease-and-hydrocarbon', Grease_and_hydrogen.Grease_and_hydrogenViewSet, basename='add-grease-and-hydrocarbon')
router.register(r'add-waste-management', views.Storage_facilityViewSet, basename='add-waste-management')
router.register(r'add-inceneration', views.Storage_facilityViewSet, basename='add-inceneration')
router.register(r'add-liquid-waste-oil', views.Storage_facilityViewSet, basename='add-liquid-waste-oil')

urlpatterns = [
    path('', index.index, name='index'),
    path('add/', include(router.urls)),
    path('storage_facility', views.storage_facilityView, name='storage_facility'),
    path('grease-and-hydrocarbon', views.grease_and_hydrocarbonView, name='grease-and-hydrocarbon'),
    path('waste-management', views.waste_managementView, name='waste-management'),
    path('inceneration', views.incenerationView, name='inceneration')
    # path('/analytics/',include('analytics.urls')),
    # path('add', views.Storage_facilityViewSet, name='add'),
]


# urlpatterns += router.urls