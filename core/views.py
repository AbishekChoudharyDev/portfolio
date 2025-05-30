from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def certificates(request):
    return render(request, 'certificates.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can add saving to DB or sending email here later
    return render(request, 'contact.html')
