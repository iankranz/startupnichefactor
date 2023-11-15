from django.urls import path
from . import views

urlpatterns = [
    path('startups/', views.startups),
    path('startups/<uuid:id>/', views.startup_by_id),
    path('startups/<uuid:id>/add-fire', views.startup_add_fire),
    path('startups/<uuid:id>/remove-fire', views.startup_remove_fire),
    path('startups/<uuid:id>/add-snooze', views.startup_add_snooze),
    path('startups/<uuid:id>/remove-snooze', views.startup_remove_snooze)
]