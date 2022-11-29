from django.http import JsonResponse
from django.shortcuts import render
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .models import Book, Member, Borrow

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'librarian.html', {'books': books})

def members(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

def borrows(request):
    borrows = Borrow.objects.all()
    return render(request, 'borrows.html', {'borrows': borrows})

