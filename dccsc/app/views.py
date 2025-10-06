from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def member_registration(request):
    return render(request, 'member_registration.html')

def payment(request):
    return render(request, 'payment.html')

def section_representative_details(request):
    return render(request, 'section_representative_details.html')