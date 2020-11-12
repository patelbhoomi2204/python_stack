from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.newShow),
    path('createShow', views.createShow),
    path('shows/<int:showId>', views.showInfo),
    path('shows/<int:showId>/edit', views.editShow),
    path('shows/<int:showId>/update', views.updateShow),
    path('shows/<int:showId>/destroy', views.deleteShow)
]