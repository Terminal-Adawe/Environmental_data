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
from .models import WasteDetails
from .models import ComplianceValue
from .models import modules
from .models import Graph_builder_field
from .models import Chart
from .models import Graph_config
from .models import Notifications
from .models import Custom_table
from .models import reports
from .models import Tasks
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=150, required=True)
	password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'}, required=True)


class UserResponseAuth(serializers.Serializer):
	token = serializers.CharField(max_length=150)
	response_message = serializers.CharField(max_length=255)
	user = serializers.CharField(max_length=255)
	response_code = serializers.CharField(max_length=255)

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

class TasksSerializerGet(serializers.ModelSerializer):
	class Meta:
		model = Tasks
		fields = '__all__'

class TasksSerializer(serializers.Serializer):
	task = serializers.CharField(max_length=120,required=True)
	description = serializers.CharField(max_length=500,required=False,allow_blank=True)
	task_for = serializers.CharField(max_length=50)
	start_time = serializers.DateTimeField()
	end_time = serializers.DateTimeField()
	username = serializers.CharField(max_length=100)

class UsernameSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','is_staff']

class UsernameSerializerGet(serializers.ModelSerializer):
	username = serializers.CharField(max_length=120,required=True)

class reportBuilderSerializerGet(serializers.Serializer):
	table_name = serializers.CharField(max_length=50, allow_null=True)
	module = serializers.CharField(max_length=120, required=True)
	x_column = serializers.CharField(max_length=50, allow_null=True)
	y_column = serializers.CharField(max_length=50, allow_null=True)
	description = serializers.CharField(max_length=100, allow_null=True, required=False)
	value = serializers.CharField(max_length=50, allow_null=True)
	groupType = serializers.CharField(max_length=50, allow_null=True)
	username = serializers.CharField(max_length=100)

class randColumnSerializer(serializers.Serializer):
	column = serializers.CharField(max_length=100, source='*')
	# sum = serializers.CharField(max_length=100, source='*')
	# count = serializers.CharField(max_length=100, source='*')
		
class CustomTablesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Custom_table
		fields = ['id','table_name','group_type','module','x_column','y_column','value','created_at']


class customIDSerializer(serializers.Serializer):
	id = serializers.CharField(max_length=10)

class graphConfigSerializer(serializers.Serializer):
	id = serializers.CharField(max_length=10)
	value = serializers.CharField(max_length=10)

class ModulesSerializer(serializers.ModelSerializer):
	class Meta:
		model = modules
		fields = '__all__'

class formSerializer(serializers.Serializer):
	# auth_user = serializers.CharField(max_length=30)
	# auth_password = serializers.CharField(max_length=30)
	module = serializers.CharField(max_length=100)
	fields = serializers.ListField(
			child=serializers.JSONField()
		)
	additionalFields = serializers.ListField(
			child=serializers.JSONField(allow_null=True,required=False),
			allow_null=True, 
			required=False
		)
	# additionalFields = serializers.ListField(
	# 		child=serializers.CharField(max_length=255,allow_null=True,allow_blank=True,required=False),
	# 		allow_null=True, 
	# 		required=False
	# 	)
	# additionalFields = serializers.CharField(max_length=255,allow_null=True,allow_blank=True,required=False)

class reportsSerializer(serializers.Serializer):
	report_name = serializers.CharField(max_length=255, allow_null=True)
	report_structure = serializers.CharField(max_length=255, allow_null=True)

class reportsInsertSerializer(serializers.Serializer):
	reportName = serializers.CharField(max_length=255, allow_null=True)
	category = serializers.CharField(max_length=255, allow_null=True)
	the_id = serializers.CharField(max_length=255, allow_null=True)
	module_id = serializers.CharField(max_length=255, allow_null=True)

class reportsModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = reports
		fields = '__all__'


class notesInsertSerializer(serializers.Serializer):
	notes = serializers.CharField(max_length=255, allow_null=True)
	action = serializers.CharField(max_length=255, allow_null=True)
	note_id = serializers.CharField(max_length=255, allow_null=True, required=False)
	report_id = serializers.CharField(max_length=255, allow_null=True, required=False)
	username = serializers.CharField(max_length=255, allow_null=True, required=False)


class reportsUpdateSerializer(serializers.Serializer):
	report_id = serializers.CharField(max_length=255, allow_null=True)
	category = serializers.CharField(max_length=255, allow_null=True)
	the_id = serializers.CharField(max_length=255, allow_null=True)
	module_id = serializers.CharField(max_length=255, allow_null=True)
	position = serializers.CharField(max_length=255, allow_null=True)
	action = serializers.CharField(max_length=255, allow_null=True)
	username = serializers.CharField(max_length=255, allow_null=True)
	full_struct = serializers.ListField(
			child=serializers.JSONField(allow_null=True,required=False),
			allow_null=True
		)
