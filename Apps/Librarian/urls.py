
from django.urls import path
from Apps.Librarian import views

urlpatterns = [
    path('', views.home),
    path('members/', views.members),
    path('borrows/', views.borrows),

]