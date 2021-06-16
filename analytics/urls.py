from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from . import views
from .view_controllers import index
from .view_controllers import dashboard
from .view_controllers import report_exports
from .view_controllers import saveForms
from .view_controllers import loginAPI

app_name = 'analytics'

# router = routers.DefaultRouter()
# router.register(r'', dashboard.DashboardViewSet, basename='get-details')

router = routers.DefaultRouter()
router.register(r'add_task', views.Add_task, basename='add_task')
router.register(r'update-graph-config', views.Update_graph, basename='update-graph-config')
router.register(r'post-request', saveForms.postRequestViewSet, basename='post-request')
# router.register(r'authenticate-user', loginAPI.loginViewSet_s, basename='authenticate-user')

urlpatterns = [
    path('', index.index, name='index'),
    path('api/', include(router.urls)),
    # path('authenticate-user/', include('rest_auth.urls')),
    # path('update/', include(router.urls)),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('add_task', views.add_task, name='add_task'),
    path('dashboard', index.dashboard, name='dashboard'),
    path('login', index.login, name='login'),
    path('logout', index.logout_user, name='logout'),
    path('media', index.media, name='media'),
    path('graph-builder', index.graph_builder, name='graph-builder'),
    path('report-builder', index.report_builder, name='report-builder'),
    path('table-builder', index.table_builder, name='table-builder'),
    path('get-tables/', dashboard.GetTablesViewSet.as_view(), name='get-tables'),
    path('get-table/', dashboard.GetTableViewSet.as_view({'get': 'retrieve'}), name='get-table'),
    path('component_values',views.component_values, name='component_values'),
    path('reports',views.reports, name='reports'),
    path('graphs',views.graphs, name='graphs'),
    path('tables',views.tables, name='tables'),
    path('view-graph', views.GetUsers.as_view(), name='view-graph'),
    path('view_report/<module>/<report_id>/',views.view_report, name='view_report'),
    path('view_all_reports/<module>/',views.view_all_reports, name='view_all_reports'),
    path('register_user', index.registerUser, name='register_user'),
    path('add-user', index.adduser, name='add-user'),
    path('edit-user', index.edituser, name='edit-user'),
    path('schedule_task', index.adduser, name='schedule_task'),
    path('get-details/', dashboard.DashboardViewSet.as_view(), name='get-details'),
    path('get-notifications/', dashboard.NotificationsViewSet.as_view(), name='get-notifications'),
    path('get-users/', views.GetUsers.as_view(), name='get-users'),
    path('/dataProcessor/',include('dataProcessor.urls')),
    path('get-module-details/', dashboard.buildGraphViewSet.as_view(), name='get-module-details'),
    path('get-modules/', index.getModulesViewSet.as_view({'get': 'retrieve'}), name='get-modules'),
    path('post-request/', saveForms.postRequestViewSet, name='post-request'),
    path('authenticate-user/login/', loginAPI.loginViewSet_s.as_view(), name='authenticate-user'),
    # path(r'^export/csv$', report_exports.export_single_report, name='export_report'),
    path(r'^export/csv/$', report_exports.export_report, name='export_report'),
    path(r'authenticate-user/user/login/', obtain_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
]
