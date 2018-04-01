from django.urls import path
from . import views


urlpatterns = [
    path('', views.HddListView.as_view(), name='index'),
    path('hdd/create/', views.HddCreate.as_view(), name='hdd_create'),
    path('hdd/<int:pk>/update/', views.HddUpdate.as_view(), name='hdd_update'),
    path('facility/', views.FacilityListView.as_view(), name='facility'),
    path('facility/<int:pk>/update/', views.FacilityUpdate.as_view(), name='facility_update'),
    

]