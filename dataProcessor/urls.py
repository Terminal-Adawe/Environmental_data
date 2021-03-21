from django.urls import include, path
from rest_framework import routers

from . import views
from .view_controllers import Storage_facility
from .view_controllers import Grease_and_hydrogen
from .view_controllers import Waste_management
from .view_controllers import Inceneration
from .view_controllers import Liquid_waste_oil
from .view_controllers import Health_and_hygiene
from .view_controllers import Energy_management
from .view_controllers import Complaints_register
from .view_controllers import Slope_stabilization_and_surface_water_retention
from .view_controllers import Safety_training
from .view_controllers import Safety_permission_system
from .view_controllers import Safety_tools
from .view_controllers import index

app_name = 'dataProcessor'

router = routers.DefaultRouter()
router.register(r'add-seepage', Storage_facility.Storage_facilityViewSet, basename='add-seepage')
router.register(r'add-grease-and-hydrocarbon', Grease_and_hydrogen.Grease_and_hydrogenViewSet, basename='add-grease-and-hydrocarbon')
router.register(r'add-waste-management', Waste_management.Waste_managementViewSet, basename='add-waste-management')
router.register(r'add-inceneration', Inceneration.IncenerationViewSet, basename='add-inceneration')
router.register(r'add-liquid-waste-oil', Liquid_waste_oil.liquid_waste_oilViewSet, basename='add-liquid-waste-oil')
router.register(r'add-health-and-hygiene-awareness', Health_and_hygiene.Health_and_hygieneViewSet, basename='add-health-and-hygiene-awareness')
router.register(r'add-energy-management', Energy_management.Energy_managementViewSet, basename='add-energy-management')
router.register(r'add-complaints-register', Complaints_register.Complaints_registerViewSet, basename='add-complaints-register')
router.register(r'add-slope-stabilization', Slope_stabilization_and_surface_water_retention.Slope_stabilization_and_surface_water_retentionViewSet, basename='add-slope-stabilization')
router.register(r'add-safety-training', Safety_training.Safety_trainingViewSet, basename='add-safety-training')
router.register(r'add-safety-permission-system', Safety_permission_system.Safety_permission_systemViewSet, basename='add-safety-permission-system')
router.register(r'add-safety-tools', Safety_tools.Safety_toolsViewSet, basename='add-safety-tools')


urlpatterns = [
    path('', index.index, name='index'),
    path('add/', include(router.urls)),
    path('grease-and-hydrocarbon', views.grease_and_hydrocarbonView, name='grease-and-hydrocarbon'),
    path('waste-management', views.waste_managementView, name='waste-management'),
    path('inceneration', views.incenerationView, name='inceneration'),
    path('liquid-waste-oil', views.liquid_waste_oilView, name='liquid-waste-oil'),
    path('health-and-hygiene-awareness', views.health_and_hygiene_awarenessView, name='health-and-hygiene-awareness'),
    path('energy-management', views.energy_managementView, name='energy-management'),
    path('complaints-register', views.complaints_registerView, name='complaints-register'),
    path('slope-stabilization', views.slope_stabilizationView, name='slope-stabilization'),
    path('safety-training', views.safety_trainingView, name='safety-training'),
    path('safety-permission-system', views.safety_permission_systemView, name='safety-permission-system'),
    path('safety-tools', views.safety_toolsView, name='safety-tools'),
    path('storage-facility', views.storage_facilityView, name='storage-facility'),
    # path('/analytics/',include('analytics.urls')),
    # path('add', views.Storage_facilityViewSet, name='add'),
]


# urlpatterns += router.urls