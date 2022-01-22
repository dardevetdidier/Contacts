from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact/', views.add_contact, name='add-contact'),
    path('contact-detail/<int:pk>/', views.contact_detail, name='contact-detail'),
    path('edit-contact/<int:pk>/', views.edit_contact, name='edit-contact'),
    path('delete-contact/<int:pk>/', views.delete_contact, name='delete-contact'),
    path('search', views.search, name='search')
]
