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
		
class Storage_facility(models.Model):
	GOOD = 'GD'
	SLIGHTLY_DISTURBED = 'SD'
	BLOCKED = 'BL'
	STABLE = 'STB'
	SIGNS_OF_EROSION = 'SOE'
	REHABILITATED = 'RBT'
	YES = 'Y'
	NO = 'N'

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
	status_of_seepage_point = models.CharField(max_length=50, choices=SEEPAGE_POINTS_S)
	stability_of_dam_walls = models.CharField(max_length=50,choices=DAM_WALLS_STABILITY)
	holding_capacity = models.CharField(max_length=10)
	current_capacity = models.CharField(max_length=10)
	spillways_capacity = models.CharField(max_length=10)
	spillways_stability = models.CharField(max_length=50)
	signs_of_erosion_spillway_tip = models.CharField(max_length=10,choices=YES_NO)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Grease_and_hydocarbon_spillage(models.Model):
	COMPLETELY_IMPERVIOUS_SURFACE = 'CIS'
	PARTIALLY_IMPERVIOUS = 'PI'
	NON_IMPERVIOUS = 'NI'
	STORED_IN_CONTAINMENT = 'SIC'
	NOT_STORED_IN_CONTAINMENT = 'NSIC'

	STORAGE_CONDITION_S = [
		(COMPLETELY_IMPERVIOUS_SURFACE,'Completely Impervious Surface'),
		(PARTIALLY_IMPERVIOUS,'Partially Impervious'),
		(NON_IMPERVIOUS,'Non Impervious'),
		(STORED_IN_CONTAINMENT,'Stored in Containment'),
		(NOT_STORED_IN_CONTAINMENT,'Not Stored in Containment')
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	storage_condition = models.CharField(max_length=50, choices=STORAGE_CONDITION_S)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Waste_Management(models.Model):
	EFFECTIVE = 'EF'
	NOT_EFFECTIVE = 'NEF'
	PARTIALLY_EFFECTIVE = 'PEF'
	SORTED_AT_DUMP_SITE = 'SDS'

	SEGREGATION_S = [
		(EFFECTIVE,'Effective'),
		(NOT_EFFECTIVE,'Not Effective'),
		(PARTIALLY_EFFECTIVE,'Partially Effective'),
		(SORTED_AT_DUMP_SITE,'Sorted at Dump Site')
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	segregation_at_source_and_bins = models.CharField(max_length=100, choices=SEGREGATION_S)
	glass_waste_source = models.CharField(max_length=10)
	glass_waste_weight = models.CharField(max_length=10)
	plastic_waste_source = models.CharField(max_length=10)
	plastic_waste_weight = models.CharField(max_length=10)
	metal_waste_source = models.CharField(max_length=10)
	metal_waste_weight = models.CharField(max_length=10)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Inceneration(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	items_incenerated = models.CharField(max_length=10)
	quantity = models.CharField(max_length=10)
	temperature = models.CharField(max_length=20)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Liquid_waste_oil(models.Model):
	MAINTENANCE_WORKSHOP = 'MW'
	OTHER_AREA = 'OA'

	SOURCE = [
		(MAINTENANCE_WORKSHOP,'Maintenance Workshop'),
		(OTHER_AREA,'Other Area')
	]
	
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	discharge_point = models.CharField(max_length=100, null=True, blank=True)
	source = models.CharField(max_length=50, choices=SOURCE)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Health_and_hygiene_awareness(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	training = models.CharField(max_length=100)
	no_of_staff = models.CharField(max_length=10)
	no_of_visitors = models.CharField(max_length=10, default='0')
	duration = models.CharField(max_length=15)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Energy_management(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	total_energy_available = models.CharField(max_length=50)
	camp_consumption = models.CharField(max_length=20)
	admin_consumption = models.CharField(max_length=20)
	workshop_consumption = models.CharField(max_length=20)
	mine_plant_consumption = models.CharField(max_length=20)
	other_consumption = models.CharField(max_length=20)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Complaints_register(models.Model):
	RESOLVED = 'RSD'
	PENDING = 'PEN'
	OTHER = 'OTR'

	STATUS_S = [
		(RESOLVED,'Resolved'),
		(PENDING,'Pending'),
		(OTHER,'Other')
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	no_of_complaints = models.CharField(max_length=50)
	status_of_complaints = models.CharField(max_length=80,choices=STATUS_S)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Slope_stabilization_and_surface_water_retention(models.Model):
	STABILIZED = 'STD'
	WORKING_PROGRESS = 'WP'
	PENDING = 'PEN'
	OTHER = 'OTR'

	STATUS_S = [
		(STABILIZED,'Stabilized'),
		(WORKING_PROGRESS,'Working Progress'),
		(PENDING,'Pending'),
		(OTHER,'Other')
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	no_of_exposed_unstabilized_slopes = models.CharField(max_length=10)
	status = models.CharField(max_length=100,choices=STATUS_S)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Safety_training(models.Model):
	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	training = models.CharField(max_length=100)
	no_of_staff = models.CharField(max_length=10)
	no_of_inductions = models.CharField(max_length=10)
	no_of_visitors = models.CharField(max_length=10, default='0')
	duration = models.CharField(max_length=15)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
		
class Safety_permission_system(models.Model):
	WORK_ENDED_SAFELY = 'WES'
	WORK_ENDED_UNSAFELY = 'WEU'

	STATUS_S = [
		(WORK_ENDED_SAFELY,'Work Ended Safely'),
		(WORK_ENDED_UNSAFELY,'WWork did not end safely'),
	]

	report_name = models.CharField(max_length=100, default='REPORT_1', null=True, blank=True)
	no_of_permits_issued = models.CharField(max_length=10)
	status = models.CharField(max_length=100,choices=STATUS_S)
	comment = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User,
		on_delete=models.PROTECT)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
		

		
		