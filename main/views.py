from django.shortcuts import render 

# Create your views here.
def index(request):
    context ={}
    return render(request, 'main/index.html',context)


def projects (request):
    context ={}
    return render (request, 'main/projects.html',context)


def skills(request):
    context ={}
    return render (request, 'main/skills.html',context)

def about(request):
    context ={}
    return render (request, 'main/about.html',context) 

def services(request):
    context ={}
    return render (request, 'main/services.html',context) 



def contact(request):
    context ={}
    return render(request, 'main/contact.html', context)
   
   

def certificates(request):
    context ={}
    return render (request, 'main/certificates.html',context)

