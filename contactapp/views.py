from django.shortcuts import render, redirect
from .models import Contact, Group
from .forms import ContactForm


def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contactapp/index.html', context=context)


def add_contact(request):
    groups = Group.objects.all()

    print(groups)
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form = ContactForm()

    context = {
        'groups': groups,
        'form': form}

    return render(request, 'contactapp/addcontact.html', context=context)


def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    context = {'contact': contact}
    return render(request, 'contactapp/detail.html', context=context)