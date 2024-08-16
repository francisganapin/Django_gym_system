from django.urls import path
from .views import showMember_views,addMember_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('member',showMember_views,name='showMember_views'),
    path('add_member',addMember_views,name='addMember_views')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)