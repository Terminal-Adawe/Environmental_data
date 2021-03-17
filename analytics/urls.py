from django.urls import include, path

from . import views
from .view_controllers import index

app_name = 'analytics'

urlpatterns = [
    path('', index.index, name='index'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard', index.dashboard, name='dashboard'),
    path('login', index.login, name='login'),
    path('logout', index.logout_user, name='logout'),
    path('dashboard', index.dashboard, name='dashboard'),
    path('register_user', index.registerUser, name='register_user'),
    path('/dataProcessor/',include('dataProcessor.urls')),
]