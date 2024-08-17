from django.urls import path
from .views import showMember_views,addMember_views,updateMember_views,deleteMember_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('member',showMember_views,name='showMember_views'),
    path('add_member',addMember_views,name='addMember_views'),
    path('update_member',updateMember_views,name='updateMember_views'),
    path('delete_member',deleteMember_views,name='deleteMember_views')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)