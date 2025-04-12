from django.urls import path
from . import views
from django.contrib.auth import views as ad
from .views import Add_orphanform
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="hm"),
    path('send_email/',views.send_email,name="send_email"),
    path('vhome/',views.vhome,name="vhome"),
    path('accept/<int:id>',views.accept,name="accept"),
    path('abt/',views.about,name="ab"),
    path('cnt/',views.contact,name="ct"),
    path('reg/',views.register,name="rg"),
    path('volenteer-login/',views.volenteer_login,name="volenteer_login"),
    path('lgo/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),

    path('adlog/', views.addoptentlogin, name="adp"),
    path('lot/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgtn"),
    path('event-booking/', views.event_booking, name='eb'),
    path('event-booking/success/', views.event_booking_success, name='ebs'),
    path('volenteer-login/', views.volenteer_login, name='volenteer_login'),
    path('edit_volunteer/<int:id>/', views.edit_volunteer, name='edit_volunteer'),
    path('confirmed_events',views.accepted_events,name="confirmed_events"),
    path('delete_volunteer/<int:id>/', views.delete_volunteer, name='delete_volunteer'),
    path('edit_orphan/<int:id>/', views.edit_orphan, name='edit_orphan'),
    path('delete_orphan/<int:id>',views.delete_orphan,name='delete_orphan'),


    path('delete_confirmed_event/<int:id>/', views.delete_confirmed_event, name='delete_confirmed_event'),
    path('add_orphan',views.add_orphan,name='add_orphan'),
    path('orphan_details/',views.orphan_details,name='orphan_details'),
    path('orcr/',views.orphcr,name="orcr"),
    path('edit_orphan/<int:id>/', views.edit_orphan, name='edit_orphan'),
    path('delete_orphan/<int:id>/', views.delete_orphan, name='delete_orphan'),
    # ...
    path('adoptent-login-list/', views.adoptent_login_list, name='adoptent_login_list'),
    path('delete-record/<int:record_id>/', views.delete_record, name='delete_record'),
    # path('accept-record/<int:uid>/', views.accept_record, name='accept-record'),
    path('requested_events',views.requested_events,name='requested_events'),

]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)