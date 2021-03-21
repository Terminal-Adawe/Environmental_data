from django.urls import include, path
from rest_framework import routers

from . import views
from .view_controllers import index
from .view_controllers import dashboard

app_name = 'analytics'

# router = routers.DefaultRouter()
# router.register(r'', dashboard.DashboardViewSet, basename='get-details')

urlpatterns = [
    path('', index.index, name='index'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard', index.dashboard, name='dashboard'),
    path('login', index.login, name='login'),
    path('logout', index.logout_user, name='logout'),
    path('dashboard', index.dashboard, name='dashboard'),
    path('component_values',views.component_values, name='component_values'),
    path('reports',views.reports, name='reports'),
    path('view_report/<module>/<report_id>/',views.view_report, name='view_report'),
    path('register_user', index.registerUser, name='register_user'),
    path('get-details/', dashboard.DashboardViewSet.as_view(), name='get-details'),
    path('/dataProcessor/',include('dataProcessor.urls')),
]