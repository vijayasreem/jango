#views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    # Ability to navigate to the sacral.ai website and login into the sacral.ai website
    return render(request, 'sacral_ai_website.html')

def login_view(request):
    # Ability to successfully login and access “Expert Services to change Business” page
    return render(request, 'login.html')

def configure_view(request):
    # Ability to click on Configure
    return render(request, 'configure.html')

def github_view(request):
    # Ability to click on GitHub
    return render(request, 'github.html')

def github_details_view(request):
    # The user must provide a GitHub username, password, URL and repository name
    return render(request, 'github_details.html')

def reset_view(request):
    # Ability to click on reset button to enter the details again
    return render(request, 'reset.html')

def save_view(request):
    # Ability to click on save button to configure
    return render(request, 'save.html')

def java_api_view(request):
    # The Java API must validate the Jira Software credentials and return a response indicating whether authentication was successful or not
    return render(request, 'java_api.html')

def error_message_view(request):
    # If the credentials are not valid, an error message is displayed, and the user is prompted to enter the correct information
    return render(request, 'error_message.html')

def list_view(request):
    # Ability to display the list with Title, User Name, URL, Action
    return render(request, 'list.html')

def edit_delete_view(request):
    # Ability to display edit button and delete button to make any changes to the displayed list Title, User Name and URL
    return render(request, 'edit_delete.html')

def show_entries_view(request):
    # Ability to change the No of entries to display in the list, while clicking on dropdown button in “Show entries”
    return render(request, 'show_entries.html')

def pagination_view(request):
    # Ability to display pagination under the list
    return render(request, 'pagination.html')

def add_more_view(request):
    # Ability to display Add more button above the list to configure other GitHub
    return render(request, 'add_more.html')

def pop_up_form_view(request):
    # Ability to display Pop Up form
    return render(request, 'pop_up_form.html')

def enter_details_view(request):
    # Ability to Ability to enter the required details
    return render(request, 'enter_details.html')