from rest_framework import serializers
from analytics.models import Storage_facility
from analytics.models import Grease_and_hydocarbon_spillage
from analytics.models import Waste_Management
from analytics.models import Inceneration
from analytics.models import Liquid_waste_oil
from analytics.models import Health_and_hygiene_awareness
from analytics.models import Energy_management
from analytics.models import Complaints_register
from analytics.models import Slope_stabilization_and_surface_water_retention
from analytics.models import Safety_training
from analytics.models import Safety_permission_system



class Storage_facilitySerializer(serializers.ModelSerializer):
	# status_of_seepage_point = serializers.ChoiceField(choices=Storage_facility.SEEPAGE_POINTS_S)
	# stability_of_dam_walls = serializers.ChoiceField(choices=Storage_facility.DAM_WALLS_STABILITY)
	# signs_of_erosion_spillway_tip = serializers.ChoiceField(choices=Storage_facility.YES_NO)

	class Meta:
		model = Storage_facility
		fields = ('report_name','status_of_seepage_point','stability_of_dam_walls','holding_capacity','current_capacity','spillways_capacity','spillways_stability','signs_of_erosion_spillway_tip',)


class Storage_facilitySerializer_serializer(serializers.Serializer):
	stability_of_dam_walls = serializers.ChoiceField(choices=Storage_facility.DAM_WALLS_STABILITY)
	status_of_seepage_point = serializers.ChoiceField(choices=Storage_facility.SEEPAGE_POINTS_S)
	signs_of_erosion_spillway_tip = serializers.ChoiceField(choices=Storage_facility.YES_NO)
	# storage_type = serializers.CharField(max_length=50)
	report_name = serializers.CharField(max_length=100)
	# status_of_seepage_point = serializers.CharField(max_length=50)
	# stability_of_dam_walls = serializers.CharField(max_length=50)
	holding_capacity = serializers.CharField(max_length=10)
	current_capacity = serializers.CharField(max_length=10)
	spillways_capacity = serializers.CharField(max_length=10)
	spillways_stability = serializers.CharField(max_length=50)
	comment = serializers.CharField(max_length=500)
	# signs_of_erosion_spillway_tip = serializers.CharField(max_length=10)
	username = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Storage_facility(id=None, **validated_data)

class Grease_and_hydrogenSerializer(serializers.Serializer):
	class Meta:
		model = Grease_and_hydocarbon_spillage
		fields = ('report_name','storage_condition','comment')

class Grease_and_hydrogenSerializer_serializer(serializers.Serializer):
	storage_condition = serializers.ChoiceField(choices=Grease_and_hydocarbon_spillage.STORAGE_CONDITION_S)
	report_name = serializers.CharField(max_length=100)
	comment = serializers.CharField(max_length=500)
	username = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Grease_and_hydocarbon_spillage(id=None, **validated_data)
		