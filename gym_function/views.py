from django.shortcuts import render,redirect,get_object_or_404
from gym_function.models import gym_members,gym_item,gym_trainor,gym_classes
from .forms import InputFormInventory,RegisterFormMember,RegisterFormTrainor
import mysql.connector

from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.

def showHomepage_views(request):
    return render(request,'homepage.html')


def showMember_views(request):
    members = gym_members.objects.all()  # Fetch all members
    return render(request, 'member/show_member.html', {"members": members})


def updateMember_views(request):
    '''This will update our member'''
    if request.method == 'POST':
        id_card = request.POST.get('id_card')
        expiry = request.POST.get('expiry')

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE gym_members SET expiry=%s WHERE id_card=%s",
                [expiry, id_card]
            )
        return redirect('showMember_views')

    return render(request, 'member/update_member.html')


def deleteMember_views(request):
    if request.method =='POST':
        id_card = request.POST.get('id_card')
        
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM gym_members WHERE id_card = %s",
                           [id_card]
                           )

        return redirect(showMember_views)
    return render(request,'member/delete_member.html')


def loginMember_views(request):
    expiry_date = None  # Initialize expiry_date at the beginning

    if request.method == 'POST':
        id_card = request.POST.get('id_card')  # Wrap id_card in quotes as it's a string key
        if id_card:
            with connection.cursor() as cursor:
                cursor.execute('SELECT expiry FROM gym_members WHERE id_card = %s', [id_card])
                expiry_date = cursor.fetchone()
        return render(request, 'member/login_member.html', {'expiry_date': expiry_date})
    return render(request, 'member/login_member.html', {'expiry_date': expiry_date})


def addMember_views(request):
    if request.method == 'POST':
        form = RegisterFormMember(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/member?page=1')
    else:
        form = RegisterFormMember()
    return render(request,'member/add_member.html',{'form':form})



def showInventory_views(request):
    inventory = gym_item.objects.all()  # Fetch all members
    return render(request, 'inventory/list_inventory.html', {"inventory": inventory})




def updateInventory_views(request):
    if request.method == 'POST':
        id  = request.POST.get('id')
        stock = request.POST.get('stock')

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE gym_item SET stock=%s WHERE id=%s",
                (stock, id)  # Use a tuple here
            )
        return redirect('showInventory_views')
    return render(request,'inventory/update_inventory.html')

def deleteInventory_views(request):
    if request.method == 'POST':
        id  = request.POST.get('id')

        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM gym_item WHERE id=%s",
                (id,)  # Use a tuple here # add this , <- i dunno whty it works 
            )
        return redirect('showInventory_views')
    return render(request,'inventory/delete_inventory.html')

def inputInventory_views(request):
    if request.method == 'POST':
        form = InputFormInventory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory')
    else:
        form = InputFormInventory(request.POST)
    return render(request,'inventory/add_inventory.html',{'form':form})



def showTrainor_views(request):
    trainor = gym_trainor.objects.all()  # Fetch all members
    return render(request, 'trainor/show_trainor.html', {"trainor": trainor})

def addTrainor_views(request):
    if request.method == 'POST':
        form = RegisterFormTrainor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showTrainor_views')
        else:
            # Print form errors to the console for debugging
            print(form.errors)
    else:
        form = RegisterFormTrainor()
    return render(request, 'trainor/register_trainor.html', {'form': form})


def deleteTrainor_views(request):
    if request.method == 'POST':
        trainor_id  = request.POST.get('trainor_id')

        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM gym_trainor WHERE trainor_id=%s",
                (trainor_id,)  
            )
        return redirect('showTrainor_views')
    return render(request,'trainor/delete_trainor.html')




    
def showMembershipMember_views(request):

    if request.method =='GET':
    
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(id) AS count FROM gym_members")
            row = cursor.fetchone()
            number_members = row[0] if row else 0
            cursor.close()
    
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT membership, COUNT(*) AS count 
                FROM gym_members 
                GROUP BY membership
            ''')
            rows = cursor.fetchall()
            membership_data = [{'membership': row[0], 'count': row[1]} for row in rows]
            cursor.close()

    return render(request, 'stats/stats_number.html', {'membership_data': membership_data,'number_members':number_members})




def showClass_views(request):
    gym_class = gym_classes.objects.all()
    return render(request,'classes/show_class.html',{'gym_class':gym_class})
