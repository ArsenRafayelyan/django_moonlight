from django.shortcuts import render,redirect
from . models import Logo,Home,About,Entries,Work,Contact
from . forms import ContactForm

# Create your views here.

def home(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = ContactForm()

    mylogo = Logo.objects.all()[0]
    home = Home.objects.all()[0]
    about = About.objects.all()[0]
    entries1 = Entries.objects.all()[0]
    entries2 = Entries.objects.all()[1]
    work_list = Work.objects.all()

    return render(request, 'main/index.html',context= {
        'mylogo':mylogo,
        'home':home,
        'about':about,
        'entries1':entries1,
        'entries2':entries2,
        'work_list': work_list,
        'form':form
    })