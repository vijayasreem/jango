# Urls.py

from django.urls import path
from .views import home_view, login_view, configure_view, github_view, github_details_view, reset_view, save_view, java_api_view, error_message_view, list_view, edit_delete_view, show_entries_view, pagination_view, add_more_view, pop_up_form_view, enter_details_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('configure/', configure_view, name='configure'),
    path('github/', github_view, name='github'),
    path('github_details/', github_details_view, name='github_details'),
    path('reset/', reset_view, name='reset'),
    path('save/', save_view, name='save'),
    path('java_api/', java_api_view, name='java_api'),
    path('error_message/', error_message_view, name='error_message'),
    path('list/', list_view, name='list'),
    path('edit_delete/', edit_delete_view, name='edit_delete'),
    path('show_entries/', show_entries_view, name='show_entries'),
    path('pagination/', pagination_view, name='pagination'),
    path('add_more/', add_more_view, name='add_more'),
    path('pop_up_form/', pop_up_form_view, name='pop_up_form'),
    path('enter_details/', enter_details_view, name='enter_details'),
]