from django.shortcuts import render

# Create your views here.

def home(request):
    """ Return html file"""
    return render(request, template_name='catalog/home.html')


def contacts(request):
    """ Return html file. In case in method POST, taking all needed data"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}\nPhone: {phone}\nMessage: {message}')
    return render(request, template_name='catalog/contacts.html')
