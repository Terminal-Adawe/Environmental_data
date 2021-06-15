from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Element(models.Model):
	element_name = models.CharField(max_length=80)
	purity = models.IntegerField()
	no_of_other_elements = models.CharField(max_length=250)
	description = models.TextField()
	active = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class ComplianceValue(models.Model):
	parameter = models.CharField(max_length=100, unique=True)
	key_name = models.CharField(max_length=100, unique=True)
	value = models.CharField(max_length=50, null=True, blank=True)
	min_limit = models.CharField(max_length=50, null=True, blank=True)
	max_limit = models.CharField(max_length=50, null=True, blank=True)
	unit_id = models.IntegerField(null=True, blank=True)
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Units(models.Model):
	"""docstring for units"""
	unit = models.CharField(max_length=50)
	symbol = models.CharField(max_length=5)
	active = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class modules(models.Model):
	module_name = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	description = models.CharField(max_length=200, default="None")
	table = models.CharField(max_length=50, default="None")
	priority = models.IntegerField(default=1)
	default_report_path = models.CharField(max_length=200, default="None")
	icon = models.CharField(max_length=50, default="fa-tasks")
	active = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
		
class Storage_facility(models.Model):
	GOOD = 'Good'
	SLIGHTLY_DISTURBED = 'Slightly Disturbed'
	BLOCKED = 'Blocked'
	STABLE = 'Stable'
	SIGNS_OF_EROSION = 'Signs of Erosion'
	REHABILITATED = 'Rehabilitated'
	YES = 'Yes'
	NO = 'No'

	SEEPAGE_POINTS_S = [
		(GOOD,'Good'),
		(SLIGHTLY_DISTURBED,'Slightly Disturbed'),
		(BLOCKED, 'Blocked')
	]

	DAM_WALLS_STABILITY = [
		(STABLE,'Stable'),
		(SIGNS_OF_EROSION,'Signs of Erosion'),
		(REHABILITATED,'Rehabilitated')
	]

	YES_NO = [
		(YES,'Yes'),
		(NO,'No')
	]

	storage_type = models.CharField(max_length=50)
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	status_of_seepage_point = models.CharField(max_length=50, choices=SEEPAGE_POINTS_S)
	stability_of_dam_walls = models.CharField(max_length=50,choices=DAM_WALLS_STABILITY)
	holding_capacity = models.CharField(max_length=10)
	current_capacity = models.CharField(max_length=10)
	spillways_capacity = models.CharField(max_length=10)
	spillways_stability = models.CharField(max_length=50)
	signs_of_erosion_spillway_tip = models.CharField(max_length=10,choices=YES_NO)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="1")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Grease_and_hydocarbon_spillage(models.Model):
	COMPLETELY_IMPERVIOUS_SURFACE = 'Completely Impervious Surface'
	PARTIALLY_IMPERVIOUS = 'Partially Impervious'
	NON_IMPERVIOUS = 'Non Impervious'
	STORED_IN_CONTAINMENT = 'Stored in Containment'
	NOT_STORED_IN_CONTAINMENT = 'Not Stored in Containment'

	STORAGE_CONDITION_S = [
		(COMPLETELY_IMPERVIOUS_SURFACE,'Completely Impervious Surface'),
		(PARTIALLY_IMPERVIOUS,'Partially Impervious'),
		(NON_IMPERVIOUS,'Non Impervious'),
		(STORED_IN_CONTAINMENT,'Stored in Containment'),
		(NOT_STORED_IN_CONTAINMENT,'Not Stored in Containment')
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	storage_condition = models.CharField(max_length=50, choices=STORAGE_CONDITION_S)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="2")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Waste_Management(models.Model):
	EFFECTIVE = 'Effective'
	NOT_EFFECTIVE = 'Not Effective'
	PARTIALLY_EFFECTIVE = 'Partially Effective'
	SORTED_AT_DUMP_SITE = 'Sorted at Dump Site'

	SEGREGATION_S = [
		(EFFECTIVE,'Effective'),
		(NOT_EFFECTIVE,'Not Effective'),
		(PARTIALLY_EFFECTIVE,'Partially Effective'),
		(SORTED_AT_DUMP_SITE,'Sorted at Dump Site')
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	segregation_at_source_and_bins = models.CharField(max_length=100, choices=SEGREGATION_S)
	glass_waste_source = models.CharField(max_length=100)
	glass_waste_weight = models.CharField(max_length=10)
	plastic_waste_source = models.CharField(max_length=100)
	plastic_waste_weight = models.CharField(max_length=10)
	metal_waste_source = models.CharField(max_length=100)
	metal_waste_weight = models.CharField(max_length=10)
	organic_waste_source = models.CharField(max_length=100)
	organic_waste_weight = models.CharField(max_length=10)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="3")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Inceneration(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	items_incenerated = models.CharField(max_length=200)
	quantity = models.CharField(max_length=10)
	temperature = models.CharField(max_length=20)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="4")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Liquid_waste_oil(models.Model):
	MAINTENANCE_WORKSHOP = 'Maintenance Workshop'
	OTHER_AREA = 'Other Area'

	SOURCE = [
		(MAINTENANCE_WORKSHOP,'Maintenance Workshop'),
		(OTHER_AREA,'Other Area')
	]
	
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	discharge_point = models.CharField(max_length=100, null=True, blank=True)
	source = models.CharField(max_length=50, choices=SOURCE)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="5")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Health_and_hygiene_awareness(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_6', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	training = models.CharField(max_length=100)
	no_of_staff = models.CharField(max_length=10)
	no_of_visitors = models.CharField(max_length=10, default='0')
	duration = models.CharField(max_length=15)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="6")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Energy_management(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_17', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	total_energy_available = models.CharField(max_length=50)
	camp_consumption = models.CharField(max_length=20)
	admin_consumption = models.CharField(max_length=20)
	workshop_consumption = models.CharField(max_length=20)
	mine_plant_consumption = models.CharField(max_length=20)
	other_consumption = models.CharField(max_length=20)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="7")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Water_management(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_19', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	total_water_quantity_available = models.CharField(max_length=50)
	camp_consumption = models.CharField(max_length=20)
	admin_consumption = models.CharField(max_length=20)
	workshop_consumption = models.CharField(max_length=20)
	mine_plant_consumption = models.CharField(max_length=20)
	cafeteria_consumption = models.CharField(max_length=20)
	other_consumption = models.CharField(max_length=20)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="19")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Complaints_register(models.Model):
	RESOLVED = 'Resolved'
	PENDING = 'Pending'
	OTHER = 'Other'

	STATUS_S = [
		(RESOLVED,'Resolved'),
		(PENDING,'Pending'),
		(OTHER,'Other')
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	no_of_complaints = models.CharField(max_length=50)
	status_of_complaints = models.CharField(max_length=80,choices=STATUS_S)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="8")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Slope_stabilization_and_surface_water_retention(models.Model):
	STABILIZED = 'Stabilized'
	WORKING_PROGRESS = 'Working Progress'
	PENDING = 'Pending'
	OTHER = 'Other'

	STATUS_S = [
		(STABILIZED,'Stabilized'),
		(WORKING_PROGRESS,'Working Progress'),
		(PENDING,'Pending'),
		(OTHER,'Other')
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	no_of_exposed_unstabilized_slopes = models.CharField(max_length=10)
	status = models.CharField(max_length=100,choices=STATUS_S)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="9")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Safety_training(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	training = models.CharField(max_length=100)
	no_of_staff = models.CharField(max_length=10)
	no_of_inductions = models.CharField(max_length=10)
	no_of_visitors = models.CharField(max_length=10, default='0')
	duration = models.CharField(max_length=15)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="11")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Safety_permission_system(models.Model):
	WORK_ENDED_SAFELY = 'Work Ended Safely'
	WORK_ENDED_UNSAFELY = 'Work did not end safely'

	STATUS_S = [
		(WORK_ENDED_SAFELY,'Work Ended Safely'),
		(WORK_ENDED_UNSAFELY,'Work did not end safely'),
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	no_of_permits_issued = models.CharField(max_length=10)
	status = models.CharField(max_length=100,choices=STATUS_S)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="10")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Safety_tools(models.Model):
	ACTIVE = 'Active'
	NOT_ACTIVE = 'Inactive'
	MINE = 'Mine'
	PORT = 'Port'
	SERVICED = 'Serviced'
	EXPIRED = 'Expired'

	STATUS_S = [
		(ACTIVE,'Active'),
		(NOT_ACTIVE,'Inactive'),
	]

	STATUS_T = [
		(MINE,'Mine'),
		(PORT,'Port'),
		(SERVICED,'Serviced'),
		(EXPIRED,'Expired'),
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	no_of_estinquishers = models.CharField(max_length=10)
	fire_alarm = models.CharField(max_length=100,choices=STATUS_S)
	status_of_estinguishers = models.CharField(max_length=100,choices=STATUS_T)
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="12")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
class Image(models.Model):
	module = models.ForeignKey(modules,
		related_name="modules_key",
		on_delete=models.PROTECT)
	report_id = models.CharField(max_length=10)
	image = models.ImageField(upload_to='report_images')
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		related_name="users_key",
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Graph_config(models.Model):
	graph_type = models.CharField(max_length=50)
	graph_name = models.CharField(max_length=100, null=True, blank=True)
	module = models.ForeignKey(modules,
		related_name="modulesz",
		on_delete=models.PROTECT)
	x_column = models.CharField(max_length=90,null=True, blank=True)
	y_column = models.CharField(max_length=90, null=True, blank=True)
	predictive = models.BooleanField(default=False)
	on_dashboard = models.BooleanField(default=True)
	active = models.CharField(max_length=10)
	created_by = models.ForeignKey(User,
		related_name="users",
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Graph_builder_field(models.Model):
	module = models.ForeignKey(modules,
		related_name="graphbuildermodules",
		on_delete=models.PROTECT)
	column_fields = models.TextField(null=True, blank=True)
	active = models.IntegerField(default=1)
	active = models.CharField(max_length=10)
	created_by = models.ForeignKey(User,
		related_name="graphbuilderuser",
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Chart(models.Model):
	chart_name = models.CharField(max_length=90)
	image = models.ImageField(upload_to='chart_images')
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		related_name="chartsuser",
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Notifications(models.Model):
	"""docstring for Notifications"""
	module = models.IntegerField(null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	report = models.CharField(max_length=100,null=True, blank=True)
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		related_name="notificationsuser",
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class NotificationViewer(models.Model):
	"""docstring for NotificationProcessor"""
	userid = models.ForeignKey(User,
		related_name="notificationsvieweruser",
		on_delete=models.PROTECT)
	notificationsId = models.CharField(max_length=10,null=True, blank=True)
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		related_name="notificationvieweruser",
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class WasteDetails(models.Model):
	"""docstring for WasteDetails"""
	waste_type = models.CharField(max_length=100)
	waste_source = models.CharField(max_length=100)
	waste_weightage = models.IntegerField()
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
		related_name="wastedetailsvieweruser",
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class GeoReferencePoints(models.Model):
	"""docstring for GeoReferencePoints"""
	report_name = models.CharField(max_length=100, default='REPORT_13', null=True, blank=True)
	location = models.CharField(max_length=200, default='0,0')
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="13")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class FuelFarm(models.Model):
	IMPERVIOUS = 'Impervious'
	SEMI_IMPERVIOUS = 'Semi Impervious'
	NOT_IMPERVIOUS = 'Not Impervious'
	HIGH_SPILLAGE = 'High Spillage'
	LOW_SPILLAGE = 'Low Spillage'
	NO_SPILLAGE = 'No Spillage'

	STATUS_S = [
		(NO_SPILLAGE,'No Spillage'),
		(HIGH_SPILLAGE,'High Spillage'),
		(LOW_SPILLAGE,'Low Spillage'),
	]

	STATUS_I = [
		(NOT_IMPERVIOUS,'Not Impervious'),
		(IMPERVIOUS,'Impervious'),
		(SEMI_IMPERVIOUS,'Semi Impervious'),
	]

	report_name = models.CharField(max_length=100, default='REPORT_14', null=True, blank=True)
	spillage_status = models.CharField(max_length=100,choices=STATUS_S)
	impervious_status = models.CharField(max_length=100,choices=STATUS_I)
	location = models.CharField(max_length=200, default='0,0')								
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="14")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class WorkEnvCompliance(models.Model):
	"""docstring for WorkEnvCompliance"""
	YES = 'Yes'
	NO = 'No'

	STATUS_S = [
		(YES,'Yes'),
		(NO,'No'),
	]

	report_name = models.CharField(max_length=100, default='REPORT_15', null=True, blank=True)
	first_aid = models.CharField(max_length=10,choices=STATUS_S)
	safety_stickers = models.CharField(max_length=10,choices=STATUS_S)
	estinguishers = models.CharField(max_length=10,choices=STATUS_S)
	no_of_estinquishers = models.CharField(max_length=10, null=True, blank=True)
	fire_alarm = models.CharField(max_length=10,choices=STATUS_S)
	flooding = models.CharField(max_length=10,choices=STATUS_S)
	flammables = models.CharField(max_length=10,choices=STATUS_S)
	location = models.CharField(max_length=200, default='0,0')								
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="15")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Warehouse(models.Model):
	"""docstring for Warehouse"""
	YES = 'Yes'
	NO = 'No'

	STATUS_S = [
		(YES,'Yes'),
		(NO,'No'),
	]
	
	report_name = models.CharField(max_length=100, default='REPORT_16', null=True, blank=True)
	eye_wash = models.CharField(max_length=10,choices=STATUS_S)
	shower = models.CharField(max_length=10,choices=STATUS_S)
	location = models.CharField(max_length=200, default='0,0')								
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="16")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Conveyers(models.Model):
	"""docstring for Warehouse"""
	YES = 'Yes'
	NO = 'No'

	STATUS_S = [
		(YES,'Yes'),
		(NO,'No'),
	]
	
	report_name = models.CharField(max_length=100, default='REPORT_17', null=True, blank=True)
	electrical_safety_insulation = models.CharField(max_length=10,choices=STATUS_S)
	shower = models.CharField(max_length=100,choices=STATUS_S)
	location = models.CharField(max_length=200, default='0,0')								
	comment = models.TextField(null=True, blank=True)
	module = models.CharField(max_length=50, default="17")
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class IncidentReport(models.Model):
	"""docstring for IncidentReport"""
	YES = 'Yes'
	NO = 'No'
	PERSONAL_INJURY = 'Personal Injury'
	PROPERTY_DAMAGE = 'Property Damage'
	FIRES = 'Fires'
	LOSS_TO_PROCESS = 'Loss to Process'
	ENVIRONMENT = 'Environment'
	NEAR_MISS = 'Near Miss'
	COMMUNITY = 'Community'
	DEATH = 'Death'

	STATUS_C = [
		(PERSONAL_INJURY,'Personal Injury'),
		(PROPERTY_DAMAGE,'Property Damage'),
		(FIRES,'Fires'),
		(LOSS_TO_PROCESS,'Loss to Process'),
		(ENVIRONMENT,'Environment'),
		(NEAR_MISS,'Near Miss'),
		(COMMUNITY,'Community'),
		(DEATH,'Death'),
	]

	report_name = models.CharField(max_length=100, default='REPORT_18', null=True, blank=True)
	incident_category = models.CharField(max_length=100,choices=STATUS_C)
	incident_location = models.CharField(max_length=100)
	victim_name = models.CharField(max_length=200)
	incident_start = models.DateTimeField(auto_now=True)
	incident_end = models.DateTimeField(auto_now=True)
	cause_of_incident = models.TextField(null=True, blank=True)
	actions_taken_immediately = models.TextField(null=True, blank=True)
	further_actions_taken = models.TextField(null=True, blank=True)
	corrective_measures = models.TextField(null=True, blank=True)
	responsible_person = models.CharField(max_length=200)
	location = models.CharField(max_length=200, default='0,0')								
	comment = models.TextField(null=True, blank=True)
	active = models.IntegerField(default=1)
	module = models.CharField(max_length=50, default="18")
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Priority_definition(models.Model):
	priority = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Tasks(models.Model):
	task = models.CharField(max_length=200)
	task_for = models.CharField(max_length=100)
	description = models.CharField(max_length=200,null=True, blank=True)
	active = models.IntegerField(default=1)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT,related_name="taskcreatedby")
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Custom_table(models.Model):
	table_name = models.CharField(max_length=50, null=True, blank=True)
	group_type = models.CharField(max_length=10)
	module = models.CharField(max_length=10, null=True, blank=True)
	description = models.CharField(max_length=100, null=True, blank=True)
	x_column = models.CharField(max_length=50, null=True, blank=True)
	y_column = models.CharField(max_length=50, null=True, blank=True)
	value = models.CharField(max_length=50, null=True, blank=True)
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT,related_name="custom_table")
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class reports(models.Model):
	report_name = models.CharField(max_length=50, null=True, blank=True)
	report_structure = models.TextField(null=True, blank=True)
	active = models.IntegerField(default=1)
	created_by = models.ForeignKey(User,
	on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

		