from analytics.models import modules
from analytics.models import ComplianceValue
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
from analytics.models import GeoReferencePoints
from analytics.models import FuelFarm
from analytics.models import WasteDetails
from analytics.models import WorkEnvCompliance
from analytics.models import Warehouse
from analytics.models import Conveyers
from analytics.models import IncidentReport
from analytics.models import modules
from django.db.models.fields.reverse_related import ManyToOneRel
import logging
import sys

# Get an instance of a logger
logger = logging.getLogger("module")

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

def get_model_using_modules(module):
	modules_queryset = modules.objects.filter(active=1)
	for module_i in modules_queryset:
		logger.info(module_i.module_name)
		logger.info(" vs ")
		logger.info(module)
		if module_i.module_name == module:
			myModel = str_to_class(module_i.table)
			return myModel

def get_model_using_modulesid(module):
	modules_queryset = modules.objects.filter(active=1)
	for module_i in modules_queryset:
		logger.info(module_i.module_name)
		logger.info(" vs ")
		logger.info(module)
		if module_i.id == module:
			logger.info(" modules match ")
			logger.info(module)
			myModel = str_to_class(module_i.table)
			return myModel

def get_fields_of_model(myModel):
	field_list = []
	for field in myModel._meta.get_fields():
		if not isinstance(field, ManyToOneRel):
			field_list.append(field)
	return [field.name for field in field_list]