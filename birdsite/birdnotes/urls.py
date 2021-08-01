from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'birdnotes'

urlpatterns = [
    path('', views.observations_list, name='observations_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:observation>/', views.observation_detail, name='observation_detail'),
    path('add_observation/', views.add_observation, name='add_observation'),
    path('edit_observation/<int:id>/', views.edit_observation, name='edit_observation'),
    path('remove_observation/<int:id>/', views.remove_observation, name='remove_observation'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
