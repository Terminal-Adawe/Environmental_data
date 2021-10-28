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
router.register(r'get-reports', dashboard.GetReportsViewSet, basename='get-reports')
router.register(r'add_to_report', index.addToReportViewSet, basename='add_to_report')
router.register(r'save_notes', index.saveNotesViewSet, basename='save_notes')
router.register(r'save_report_structure', index.updateReportViewSet, basename='save_report_structure')
# router.register(r'authenticate-user', loginAPI.loginViewSet_s, basename='authenticate-user')

urlpatterns = [
    path('', index.index, name='index'),
    path('api/', include(router.urls)),
    # path('authenticate-user/', include('rest_auth.urls')),
    # path('update/', include(router.urls)),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('add_task', views.add_task, name='add_task'),
    path('dashboard', index.dashboard, name='dashboard'),
    path('documentation', index.documentation, name='documentation'),
    path('admin-documentation', index.admin_documentation, name='admin-documentation'),
    path('inputter-documentation', index.inputter_documentation, name='inputter-documentation'),
    path('login', index.login, name='login'),
    path('logout', index.logout_user, name='logout'),
    path('media', index.media, name='media'),
    path('add_folder', index.add_folder, name='add_folder'),
    path('add_to_folder', index.add_to_folder, name='add_to_folder'),
    path('add_to_report', index.add_to_report, name='add_to_report'),
    path('delete_images', index.delete_images, name='delete_images'),
    path('delete_folder', index.delete_folder, name='delete_folder'),
    path('delete_graph', index.delete_graph, name='delete_graph'),
    path('delete_table', index.delete_table, name='delete_table'),
    path('save_graph', index.save_graph, name='save_graph'),
    path('graph-builder', index.graph_builder, name='graph-builder'),
    path('report-builder', index.report_builder, name='report-builder'),
    path('table-builder', index.table_builder, name='table-builder'),
    path('get-tables/', dashboard.GetTablesViewSet.as_view(), name='get-tables'),
    path('get-table/', dashboard.GetTableViewSet.as_view({'get': 'retrieve'}), name='get-table'),
    path('get-report/', dashboard.GetReportViewSet.as_view({'get': 'retrieve'}), name='get-report'),
    path('get-notes/', dashboard.GetNotesViewSet.as_view({'get': 'retrieve'}), name='get-notes'),
    path('component_values',views.component_values, name='component_values'),
    path('reports',views.reports_f, name='reports'),
    path('graphs',views.graphs, name='graphs'),
    path('tables',views.tables, name='tables'),
    path('view-graph', views.GetUsers.as_view(), name='view-graph'),
    path('view_table/<module>/<report_id>/',views.view_table, name='view_table'),
    path('view_report/<report_id>/',views.view_report, name='view_report'),
    path('view_all_reports/<module>/',views.view_all_reports, name='view_all_reports'),
    path('register_user', index.registerUser, name='register_user'),
    path('add-user', index.adduser, name='add-user'),
    path('add_report', index.add_report, name='add_report'),
    path('edit-user', index.edituser, name='edit-user'),
    path('schedule_task', index.adduser, name='schedule_task'),
    path('get-details/', dashboard.DashboardViewSet.as_view(), name='get-details'),
    path('get-notifications/', dashboard.NotificationsViewSet.as_view(), name='get-notifications'),
    path('get-users/', views.GetUsers.as_view(), name='get-users'),
    path('/dataProcessor/',include('dataProcessor.urls')),
    path('get-module-details/', dashboard.buildGraphViewSet.as_view(), name='get-module-details'),
    path('get-modules/', index.getModulesViewSet.as_view({'get': 'retrieve'}), name='get-modules'),
    path('get-reports/', dashboard.GetReportsViewSet.as_view({'get': 'retrieve'}), name='get-reports'),
    path('post-request/', saveForms.postRequestViewSet, name='post-request'),
    path('download-documentation/', index.download_pdf_file, name='download-documentation'),
    path('authenticate-user/login/', loginAPI.loginViewSet_s.as_view(), name='authenticate-user'),
    # path(r'^export/csv$', report_exports.export_single_report, name='export_report'),
    path(r'^export/csv/$', report_exports.export_report, name='export_report'),
    path(r'authenticate-user/user/login/', obtain_jwt_token),
    path(r'api-token-verify/', verify_jwt_token),
]
