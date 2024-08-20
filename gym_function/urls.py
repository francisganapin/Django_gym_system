from django.urls import path
from .views import (
    showMember_views,
    addMember_views,
    updateMember_views,
    deleteMember_views,
    showHomepage_views,
    showInventory_views,
    showTrainor_views,
    updateInventory_views,
    deleteInventory_views,
    addTrainor_views,
    deleteTrainor_views,
    showMembershipMember_views,
    showClass_views

)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',showHomepage_views,name='showHomepage_views'),
    
        #for member
    path('member',showMember_views,name='showMember_views'),
    path('add_member',addMember_views,name='addMember_views'),
    path('update_member',updateMember_views,name='updateMember_views'),
    path('delete_member',deleteMember_views,name='deleteMember_views'),

        # for inventory
    path('inventory',showInventory_views,name='showInventory_views'),
    path('inventory/update',updateInventory_views,name='updateInventory_views'),
    path('inventory/delete',deleteInventory_views,name='deleteInventory_views'),
        # for trainor 
    path('trainor',showTrainor_views,name='showTrainor_views'),
    path('trainor/register',addTrainor_views,name='addTrainor_views'),
    path('trainor/delete',deleteTrainor_views,name='deleteTrainor_views'),



    path('classes',showClass_views,name='showClass_views'),

    

        # stats
    path('show/membership/',showMembershipMember_views,name='showMembershipMember_views')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)