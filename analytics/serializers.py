from rest_framework import serializers
from .models import Storage_facility
from .models import Grease_and_hydocarbon_spillage
from .models import Waste_Management
from .models import Inceneration
from .models import Liquid_waste_oil
from .models import Health_and_hygiene_awareness
from .models import Energy_management
from .models import Complaints_register
from .models import Slope_stabilization_and_surface_water_retention
from .models import Safety_training
from .models import Safety_permission_system
from .models import ComplianceValue
from .models import modules
from .models import Graph_builder_field
from .models import Chart
from .models import Graph_config
from .models import Notifications



class Storage_facilitySerializer(serializers.ModelSerializer):
	# status_of_seepage_point = serializers.ChoiceField(choices=Storage_facility.SEEPAGE_POINTS_S)
	# stability_of_dam_walls = serializers.ChoiceField(choices=Storage_facility.DAM_WALLS_STABILITY)
	# signs_of_erosion_spillway_tip = serializers.ChoiceField(choices=Storage_facility.YES_NO)

	class Meta:
		model = Storage_facility
		fields = ('report_name','status_of_seepage_point','stability_of_dam_walls','holding_capacity','current_capacity','spillways_capacity','spillways_stability','signs_of_erosion_spillway_tip',)


class Grease_and_hydrogenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Grease_and_hydocarbon_spillage
		fields = ('report_name','storage_condition','comment')

class ComplianceValueSerializer(serializers.ModelSerializer):
	class Meta:
		model = ComplianceValue
		fields = ("parameter","key_name","value","min_limit","max_limit","unit_id")

class ModulesSerializer(serializers.ModelSerializer):
	class Meta:
		model = modules
		fields = ("id","module_name","url","description","active")

class FieldsSerializer_serializer(serializers.ModelSerializer):
	class Meta:
		model = Graph_builder_field
		fields = '__all__'
	
class ChartSerializer(serializers.ModelSerializer):
	"""docstring for ChartSerializer"""
	class Meta:
		model = Chart
		fields = '__all__'

class GraphConfigSerializer(serializers.ModelSerializer):
	class Meta:
		model = Graph_config
		fields = '__all__'

class NotificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notifications
		fields = '__all__'