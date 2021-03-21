from django.contrib import admin

from .models import Element
from .models import ComplianceValue
from .models import Units
from .models import Storage_facility
from .models import modules


# Register your models here.
admin.site.register(Element)
admin.site.register(ComplianceValue)
admin.site.register(Units)
admin.site.register(Storage_facility)
admin.site.register(modules)