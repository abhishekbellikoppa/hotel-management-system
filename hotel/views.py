from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'hotel/home.html')

def rooms(request):
    return render(request, 'hotel/rooms.html')

def booking(request):
    return render(request, 'hotel/booking.html')

def contact(request):
    return render(request, 'hotel/contact.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'hotel/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'hotel/login.html')

#register

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import Booking   # make sure model name is correct


def register(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        # Create user (using email as username)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=fullname
        )
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'hotel/register.html')

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            else:
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )
                messages.success(request, "Account created successfully")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'hotel/register.html')

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render

def home(request):
    return render(request, 'hotel/home.html')

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/rooms.html', {'rooms': rooms})


def contact(request):
    return render(request, 'hotel/contact.html')
def home(request):
    return render(request, 'hotel/home.html')

def blog(request):
    return render(request, 'hotel/blog.html')
def about(request):
    return render(request, 'hotel/about.html')
def deluxe_rooms(request):
    return render(request, 'hotel/deluxe_rooms.html')
def luxury_rooms(request):
    return render(request,'hotel/luxury_rooms.html')

from django.shortcuts import render, redirect
from .models import Booking  # make sure model name is correct

from .models import Room, Booking

from .models import Room, Booking

def booking(request, room_id):
    room = Room.objects.get(id=room_id)

    if request.method == "POST":
        arrival = request.POST.get('arrival_date')
        departure = request.POST.get('departure_date')
        full_name = request.POST.get('full_name')
        guests = request.POST.get('guests')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Booking.objects.create(
            room=room,
            arrival_date=arrival,
            departure_date=departure,
            full_name=full_name,
            guests=guests,
            email=email,
            message=message
        )

        return redirect('index')

    return render(request, 'hotel/booking.html', {'room': room})

    room_id = request.GET.get('room')

    room = None
    if room_id:
        room = Room.objects.get(id=room_id)

    if request.method == "POST":
        arrival = request.POST.get('arrival_date')
        departure = request.POST.get('departure_date')
        guests = request.POST.get('guests')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Booking.objects.create(
            room=room,
            arrival_date=arrival,
            departure_date=departure,
            guests=guests,
            email=email,
            message=message
        )

        return redirect('booking')

    return render(request, 'hotel/booking.html', {'room': room})

    room = Room.objects.get(id=room_id)

    if request.method == "POST":
        arrival = request.POST.get('arrival_date')
        departure = request.POST.get('departure_date')
        guests = request.POST.get('guests')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Booking.objects.create(
            arrival_date=arrival,
            departure_date=departure,
            room=room,   # ✅ save actual room object
            guests=guests,
            email=email,
            message=message
        )

        return redirect('booking', room_id=room.id)

    context = {
        'room': room
    }

    return render(request, 'hotel/booking.html', context)
