from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Contact
from .forms import ContactForm


def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contactapp/index.html', context=context)


def add_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form = ContactForm()

    context = {
        'form': form}

    return render(request, 'contactapp/addcontact.html', context=context)


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    context = {'contact': contact}
    return render(request, 'contactapp/detail.html', context=context)


def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        edit_form = ContactForm(request.POST, instance=contact)
        if edit_form.is_valid():
            edit = edit_form.save(commit=False)
            contact.date_created = timezone.now()
            edit.save()
        return redirect('index')

    else:
        context = {'contact': contact,
                   'form': form,
                   }
        return render(request, 'contactapp/edit.html', context=context)


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    context = {'contact': contact}

    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, 'contactapp/delete.html', context=context)
