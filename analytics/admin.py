from django.contrib import admin

from .models import Element
from .models import ComplianceValue
from .models import Units
from .models import Graph_builder_field
from .models import Chart
from .models import modules
from .models import Priority_definition


# Register your models here.
admin.site.register(Element)
admin.site.register(ComplianceValue)
admin.site.register(Units)
admin.site.register(Graph_builder_field)
admin.site.register(modules)
admin.site.register(Chart)
admin.site.register(Priority_definition)
