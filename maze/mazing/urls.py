from django.urls import path
from . import views

urlpatterns = [
    path('', views.ret, name='ret'),
    path('s/', views.note_form_view, name='note_form_view'),
    path('a/', views.table_view, name='table_view'),
    # Other URL patterns
]
