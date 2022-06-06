from django.shortcuts import render
from django.db.models import Q
from app_rearte.models import Car, Person, House_pet, Money
from app_rearte.forms import CarForm, PersonForm, House_petForm, MoneyForm



def index(request):
    return render (request, "app_rearte/home.html")

def cars(request):
    cars = Car.objects.all()
    context_dict = {
        'cars' : cars
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_rearte/cars.html",
    )

def people(request):
    people = Person.objects.all()
    context_dict = {
        'people' : people
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_rearte/people.html",
    )

def pets(request):
    pets = House_pet.objects.all()
    context_dict = {
        'pets' : pets
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_rearte/pets.html",
    )

def cash(request):
    cash = Money.objects.all()
    context_dict = {
        'cash' : cash
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_rearte/cash.html",
    )

def Cars_forms_django(request):
    if request.method == 'POST':
        Car_form = CarForm(request.POST)
        if Car_form.is_valid():
            data = Car_form.cleaned_data
            car = Car(
                brand=data['brand'],
                model=data['model'],
                license_plate=data['license_plate'],
                year=data['year'],
            )
            car.save()

            cars = Car.objects.all()
            context_dict = {
                'cars': cars
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_rearte/cars.html"
            )

    Car_form = CarForm(request.POST)
    context_dict = {
        'Car_form': Car_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_rearte/cars_django_forms.html'
    )

def People_forms_django(request):
    if request.method == 'POST':
        Person_form = PersonForm(request.POST)
        if Person_form.is_valid():
            data = Person_form.cleaned_data
            person = Person(
                name=data['name'],
                age=data['age'],
                birth_date=data['birth_date'],
                occupation=data['occupation'],
            )
            person.save()

            people = Person.objects.all()
            context_dict = {
                'people': people
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_rearte/people.html"
            )

    Person_form = PersonForm(request.POST)
    context_dict = {
        'Person_form': Person_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_rearte/people_django_forms.html'
    )

def Pets_forms_django(request):
    if request.method == 'POST':
        House_pet_form = House_petForm(request.POST)
        if House_pet_form.is_valid():
            data = House_pet_form.cleaned_data
            house_pet = House_pet(
                name=data['name'],
                age=data['age'],
                birth_date=data['birth_date'],
                animal=data['animal'],
                breed=data['breed'],
            )
            house_pet.save()

            pets = House_pet.objects.all()
            context_dict = {
                'pets': pets
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_rearte/pets.html"
            )

    House_pet_form = House_petForm(request.POST)
    context_dict = {
        'House_pet_form': House_pet_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_rearte/pets_django_forms.html'
    )

def Cash_forms_django(request):
    if request.method == 'POST':
        Money_form = MoneyForm(request.POST)
        if Money_form.is_valid():
            data = Money_form.cleaned_data
            money = Money(
                type=data['type'],
                amount=data['amount'],
            )
            money.save()

            cash = Money.objects.all()
            context_dict = {
                'cash': cash
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_rearte/cash.html"
            )

    Money_form = MoneyForm(request.POST)
    context_dict = {
        'Money_form': Money_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_rearte/cash_django_forms.html'
    )

def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        cars = Car.objects.filter(brand__contains=search_param)
        context_dict = {
            'cars': cars
        }
    elif request.GET['year_search']:
        search_param = request.GET['year_search']
        cars = Car.objects.filter(year__contains=search_param)
        context_dict = {
            'cars': cars
        }
    elif request.GET['name_search']:
        search_param = request.GET['name_search']
        people = Person.objects.filter(name__contains=search_param)
        context_dict = {
            'people': people
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_rearte/home.html",
    )
