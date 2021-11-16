from django.urls import path
from . import  views 
urlpatterns = [
    path('',views.home,name="home"),
    path('<int:year>/<str:month>/',views.home, name="home"),
    path('events',views.all_events,name="events_list"),
    path('add_venue',views.add_venue,name="add_venue"),
    path('list_venues',views.list_venues,name="list_venues"),
    path('show_venues/<venue_id>/',views.show_venue,name="show_venue"),
    
]
