# musicapp/urls.py
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('previous/', views.previous_view, name='previous_view'),
    path('search/', views.search_hymn, name='search_hymn'),
    path('search_ang/', views.search_hymn_ang, name='search_hymn_ang'),
    path('search_presby/', views.search_hymn_presby, name='search_hymn_presby'),
    path('download-midi/', views.download_midi, name='download_midi'),
    path('contact/', views.contact, name='contact'),
    # path('', views.first, name='first'),
    path('privacy/', views.privacy, name='privacy'), 
    # path('anthems/', views.anthems, name='anthems'), 
    path('armah/', views.armah, name='armah'), 
    path('armah_songs/', views.armah_songs, name='armah_songs'), 
    path('display-pdf/', views.display_pdf, name='display_pdf'),
    path('mhb/', views.display_hymn, name='display_hymn'),
    path('anglican/', views.display_hymn_ang, name='display_hymn_ang'),
    path('presby/', views.display_hymn_presby, name='display_hymn_presby'),
    path('', views.hymn_search_view, name='hymn_search'),
    path('<str:source>/<str:hymn_number>/', views.hymn_detail_view, name='hymn_detail'),
    path('display_notes/', views.display_notes, name='display_notes'),
    path('music-notes/', views.music_notes_view, name='music_notes'),    
    path('upload_audio/', views.upload_audio, name='upload_audio'),
    path('join_group_recording/', views.join_group_recording, name='join_group_recording'),
    path('mhb_rec/', views.display_hymn_meth, name='display_hymn_meth'),
    path('ang_rec/', views.display_hymn_ang_ang, name='display_hymn_ang_ang'),
    path('final_audio/', views.final_audio, name='final_audio'),
    path('download-midi-final/', views.download_midi_final, name='download_midi_final'),

    ]
