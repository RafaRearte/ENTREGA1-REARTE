from django.urls import URLPattern, path
from app_rearte import views

urlpatterns = [
    path('Home', views.index, name='Home'),
    path('cars', views.cars, name='cars'),
    path('Cars-django-forms', views.Cars_forms_django, name='CarsDjangoForms'),
    path('people', views.people, name='people'),
    path('People-django-forms', views.People_forms_django, name='PeopleDjangoForms'),
    path('pets', views.pets, name='pets'),
    path('pets-django-forms', views.Pets_forms_django, name='PetsDjangoForms'),
    path('cash', views.cash, name='cash'),
    path('cash-django-forms', views.Cash_forms_django, name='CashDjangoForms'),
    path('search', views.search, name='Search'),
]