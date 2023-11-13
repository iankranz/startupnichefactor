from django.urls import path
from . import views

urlpatterns = [
    path('startups/', views.startups),
    path('startups/<uuid:id>/', views.startup_by_id),
    path('startups/<uuid:id>/upvote', views.startup_upvote),
    path('startups/<uuid:id>/downvote', views.startup_downvote)
]