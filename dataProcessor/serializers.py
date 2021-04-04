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
from analytics.models import Safety_tools
from analytics.models import Image



class Storage_facilitySerializer(serializers.ModelSerializer):
	# status_of_seepage_point = serializers.ChoiceField(choices=Storage_facility.SEEPAGE_POINTS_S)
	# stability_of_dam_walls = serializers.ChoiceField(choices=Storage_facility.DAM_WALLS_STABILITY)
	# signs_of_erosion_spillway_tip = serializers.ChoiceField(choices=Storage_facility.YES_NO)

	class Meta:
		model = Storage_facility
		fields = '__all__'

class ImageSerializer_serializer(serializers.Serializer):
	image = serializers.ImageField(required=False)
	username = serializers.CharField(max_length=100)
	report_id = serializers.CharField(max_length=10)
	module_id = serializers.CharField(max_length=10)

	def create(self, validated_data):
		return Image(id=None, **validated_data)

class ImageSerializer(serializers.Serializer):
	class Meta:
		model = Image
		fields = ('image','module_id','report_id')

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
	comment = serializers.CharField(max_length=500, required=False,allow_blank=True)
	location = serializers.CharField(max_length=200)
	# signs_of_erosion_spillway_tip = serializers.CharField(max_length=10)
	username = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Storage_facility(id=None, **validated_data)

class Grease_and_hydrogenSerializer(serializers.ModelSerializer):
	class Meta:
		model = Grease_and_hydocarbon_spillage
		fields = '__all__'

class Grease_and_hydrogenSerializer_serializer(serializers.Serializer):
	storage_condition = serializers.ChoiceField(choices=Grease_and_hydocarbon_spillage.STORAGE_CONDITION_S)
	report_name = serializers.CharField(max_length=100)
	comment = serializers.CharField(max_length=500, required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=200)

	def create(self, validated_data):
		return Grease_and_hydocarbon_spillage(id=None, **validated_data)

class Waste_ManagementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Waste_Management
		fields = '__all__'

class Waste_ManagementSerializer_serializer(serializers.Serializer):
	segregation_at_source_and_bins = serializers.ChoiceField(choices=Waste_Management.SEGREGATION_S)
	glass_waste_source = serializers.CharField(max_length=100)
	glass_waste_weight = serializers.CharField(max_length=100)
	plastic_waste_source = serializers.CharField(max_length=100)
	plastic_waste_weight = serializers.CharField(max_length=100)
	metal_waste_source = serializers.CharField(max_length=100)
	metal_waste_weight = serializers.CharField(max_length=100)
	comment = serializers.CharField(max_length=500, required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Waste_Management(id=None, **validated_data)

class IncenerationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Inceneration
		fields = '__all__'

class IncenerationSerializer_serializer(serializers.Serializer):
	items_incenerated = serializers.CharField(max_length=200)
	quantity = serializers.CharField(max_length=100)
	temperature = serializers.CharField(max_length=100)
	comment = serializers.CharField(max_length=500, required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Inceneration(id=None, **validated_data)

class Liquid_waste_oilSerializer(serializers.ModelSerializer):
	class Meta:
		model = Liquid_waste_oil
		fields = '__all__'

class Liquid_waste_oilSerializer_serializer(serializers.Serializer):
	discharge_point = serializers.CharField(max_length=100)
	source = serializers.ChoiceField(choices=Liquid_waste_oil.SOURCE)
	comment = serializers.CharField(max_length=500, required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Liquid_waste_oil(id=None, **validated_data)

class Health_and_hygiene_awarenessSerializer(serializers.ModelSerializer):
	class Meta:
		model = Health_and_hygiene_awareness
		fields = '__all__'

class Health_and_hygiene_awarenessSerializer_serializer(serializers.Serializer):
	training = serializers.CharField(max_length=100)
	no_of_staff = serializers.CharField(max_length=100)
	no_of_visitors = serializers.CharField(max_length=100)
	duration = serializers.CharField(max_length=100)
	comment = serializers.CharField(max_length=500,required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Health_and_hygiene_awareness(id=None, **validated_data)

class Energy_managementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Energy_management
		fields = '__all__'

class Energy_managementSerializer_serializer(serializers.Serializer):
	total_energy_available = serializers.CharField(max_length=100)
	camp_consumption = serializers.CharField(max_length=100)
	admin_consumption = serializers.CharField(max_length=100)
	workshop_consumption = serializers.CharField(max_length=100)
	mine_plant_consumption = serializers.CharField(max_length=100)
	other_consumption = serializers.CharField(max_length=100)
	comment = serializers.CharField(max_length=500,required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=100)

	def create(self, validated_data):
		return Energy_management(id=None, **validated_data)

class Complaints_registerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Complaints_register
		fields = '__all__'

class Complaints_registerSerializer_serializer(serializers.Serializer):
	no_of_complaints = serializers.CharField(max_length=100)
	status_of_complaints = serializers.ChoiceField(choices=Complaints_register.STATUS_S)
	comment = serializers.CharField(max_length=500,required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=200)
	image = ImageSerializer_serializer

	def create(self, validated_data):
		return Complaints_register(id=None, **validated_data)

class Slope_stabilization_and_surface_water_retentionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Slope_stabilization_and_surface_water_retention
		fields = '__all__'

class Slope_stabilization_and_surface_water_retentionSerializer_serializer(serializers.Serializer):
	no_of_exposed_unstabilized_slopes = serializers.CharField(max_length=100)
	status = serializers.ChoiceField(choices=Slope_stabilization_and_surface_water_retention.STATUS_S)
	comment = serializers.CharField(max_length=500,required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=200)

	def create(self, validated_data):
		return Slope_stabilization_and_surface_water_retention(id=None, **validated_data)

class Safety_trainingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Safety_training
		fields = '__all__'

class Safety_trainingSerializer_serializer(serializers.Serializer):
	training = serializers.CharField(max_length=100)
	no_of_staff = serializers.CharField(max_length=100)
	no_of_inductions = serializers.CharField(max_length=100)
	no_of_visitors = serializers.CharField(max_length=100)
	duration = serializers.CharField(max_length=100)
	comment = serializers.CharField(max_length=500,required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=200)

	def create(self, validated_data):
		return Safety_training(id=None, **validated_data)

class Safety_permission_systemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Safety_permission_system
		fields = '__all__'

class Safety_permission_systemSerializer_serializer(serializers.Serializer):
	no_of_permits_issued = serializers.CharField(max_length=100)
	status = serializers.ChoiceField(choices=Safety_permission_system.STATUS_S)
	comment = serializers.CharField(max_length=500,required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=200)

	def create(self, validated_data):
		return Safety_permission_system(id=None, **validated_data)

class Safety_toolsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Safety_tools
		fields = '__all__'

class Safety_toolsSerializer_serializer(serializers.Serializer):
	no_of_estinquishers = serializers.CharField(max_length=100)
	fire_alarm = serializers.ChoiceField(choices=Safety_tools.STATUS_S)
	status_of_estinguishers = serializers.ChoiceField(choices=Safety_tools.STATUS_T)
	comment = serializers.CharField(max_length=500,required=False,allow_blank=True)
	username = serializers.CharField(max_length=100)
	report_name = serializers.CharField(max_length=100)
	location = serializers.CharField(max_length=200)

	def create(self, validated_data):
		return Safety_tools(id=None, **validated_data)


class Graph_configSerializer(serializers.ModelSerializer):
	class Meta:
		model = Safety_tools
		fields = '__all__'

class Graph_configSerializer_serializer(serializers.Serializer):
	graph_type = serializers.CharField(max_length=50)
	module_name = serializers.CharField(max_length=40)
	x_column = serializers.CharField(max_length=40)
	y_column = serializers.CharField(max_length=40)
	predictive = serializers.BooleanField()

	def create(self, validated_data):
		return Safety_tools(id=None, **validated_data)


		