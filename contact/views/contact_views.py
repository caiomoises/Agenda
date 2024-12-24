from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from ..models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    contacts = Contact.objects.filter(
        show=True,
    )

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    search = request.GET.get('q', '').strip()

    if not search:
        return redirect('contact:index')

    contacts = Contact.objects.filter(
        Q(first_name__icontains=search) |
        Q(last_name__icontains=search) |
        Q(phone__icontains=search) |
        Q(email__icontains=search) |
        Q(category__name__icontains=search),
        show=True,
    )

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Pesquisa - ',
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    single_contact = get_object_or_404(
        Contact, 
        pk=contact_id, 
        show=True
    )

    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': contact_name,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )