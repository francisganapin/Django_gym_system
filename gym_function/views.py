from django.shortcuts import render,redirect,get_object_or_404
from gym_function.models import gym_members,gym_item,gym_trainor,gym_classes,member_login
from .forms import InputFormInventory,RegisterFormMember,RegisterFormTrainor,RegisterFormClases
import mysql.connector
import datetime
from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.

def showHomepage_views(request):
    return render(request,'homepage.html')


def showMember_views(request):
    '''show member'''
    members = gym_members.objects.all()  # Fetch all members
    return render(request, 'member/show_member.html', {"members": members})


def updateMember_views(request):
    '''This will update our member'''

    message ='' # initialiaze string as message 
    if request.method == 'POST':
        id_card = request.POST.get('id_card')
        expiry = request.POST.get('expiry')

        with connection.cursor() as cursor:

            cursor.execute('SELECT * FROM gym_members where id_card =%s',(id_card,))
            result = cursor.fetchone()

            if not result:
                message = f'{id_card} does not exist'
                return render(request, 'member/update_member.html', {'message': message})

            else:
                cursor.execute(
                    "UPDATE gym_members SET expiry=%s WHERE id_card=%s",
                    [expiry, id_card]
                )

            return redirect('showMember_views')

    return render(request, 'member/update_member.html',{'message':message})


def deleteMember_views(request):
    '''this will delete member it has ability to show if member does not exist'''
    
    message = ''

    if request.method =='POST':
        id_card = request.POST.get('id_card')
            
        with connection.cursor() as cursor:

            cursor.execute('SELECT * FROM gym_members where id_card =%s',(id_card,))
            result = cursor.fetchone()

            if not result:
                message =f'{id_card} does not exist'
                return render(request,'member/delete_member.html',{'message':message})
            else:
                cursor.execute("DELETE FROM gym_members WHERE id_card = %s",[id_card] )
                connection.commit()
                return redirect(showMember_views)
   
        
    return render(request,'member/delete_member.html',{'message':message})


from datetime import datetime
from django.db import connection
from django.shortcuts import render

def loginMember_views(request):
    expiry_date = None  # Initialize expiry_date at the beginning
    result = None
    if request.method == 'POST':
        id_card = request.POST.get('id_card')  # Get the id_card from POST data
        if id_card:
            try:
                with connection.cursor() as cursor:
                    # Fetch the details from the gym_members table based on id_card
                    cursor.execute('SELECT id_card, expiry, first_name, last_name FROM gym_members WHERE id_card = %s', [id_card])
                    member_data = cursor.fetchone()
                    
                    if member_data:
                        login_card = member_data[0]  # id_card
                        expiry_date = member_data[1]  # expiry
                        first_name = member_data[2]  # first_name
                        last_name = member_data[3]   # last_name
                        login_date = datetime.now()  # current date and time

                        # Insert the data into login_record table
                        cursor.execute(
                            'INSERT INTO login_record (id_card, first_name, last_name, login) VALUES (%s, %s, %s, %s)',
                            [login_card, first_name, last_name, login_date]
                        )
                        # Commit the transaction
                        connection.commit()
                        result = [member_data]

            except Exception as e:
                print("An error occurred:", e)  # Print the exception to understand what's going wrong

        # Render the template with the fetched expiry_date
        return render(request, 'member/login_member.html', {'expiry_date': expiry_date,'result': result})
    
    # Render the template if the request is GET or id_card is not provided
    return render(request, 'member/login_member.html', {'expiry_date': expiry_date,'result': result})



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
    message = ''
    if request.method == 'POST':
        id  = request.POST.get('id')
        stock = request.POST.get('stock')
        with connection.cursor() as cursor:


            cursor.execute('SELECT * FROM gym_item WHERE id=%s',(id,))
            result = cursor.fetchone()
            
            if not result:
                message =f'{id} does not exist'
                return render(request,'inventory/update_inventory.html',{'message':message})

            else:

                # Use a tuple here # add this , <- i dunno whty it works 
                cursor.execute(
                "UPDATE gym_item SET stock=%s WHERE id=%s",(stock,id,))
                connection.commit()
                return redirect('showInventory_views')
            
    return render(request,'inventory/update_inventory.html',{'message':message})

def deleteInventory_views(request):
    message = ''
    if request.method == 'POST':
        id  = request.POST.get('id')

        with connection.cursor() as cursor:

            cursor.execute('SELECT * FROM gym_item WHERE id=%s',(id,))
            result = cursor.fetchone()
            
            if not result:
                message =f'{id} does not exist'
                return render(request,'inventory/delete_inventory.html',{'message':message})
            else:

                # Use a tuple here # add this , <- i dunno whty it works 
                cursor.execute("DELETE FROM gym_item WHERE id=%s",(id,))
                connection.commit()
                return redirect('showInventory_views')
            
    return render(request,'inventory/delete_inventory.html',{'message':message})

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

    # for number of members we have
    if request.method =='GET':
    
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(id) AS count FROM gym_members")
            row = cursor.fetchone()
            number_members = row[0] if row else 0
            cursor.close()

    # number of membership type
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

        gym_login = member_login.objects.all()  
    return render(request, 'stats/stats_number.html', {'membership_data': membership_data,'number_members':number_members,'gym_login':gym_login})




def showClass_views(request):
    gym_class = gym_classes.objects.all()
    return render(request,'classes/show_class.html',{'gym_class':gym_class})

def registerClases_views(request):

    if request.method == 'POST':
        form = RegisterFormClases(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/classes')
    else:
       form = RegisterFormClases()
    

    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute('SELECT first_name, last_name  FROM gym_trainor GROUP BY first_name, last_name')
            rows = cursor.fetchall()
            trainor_data = [{'first_name':row[0],'last_name':row[1]} for row in rows]
            cursor.close()
            
    return render(request, 'classes/register_classes.html', {'trainor_data': trainor_data, 'form': form})




def deleteClasses_views(request):
    '''this will delete classes by name be '''
    if request.method =='POST':
        class_name =request.POST.get('class_name')

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM gym_classes WHERE class_name =%s",(class_name,))
        return redirect('showClass_views')
    return render(request,'classes/delete_classes.html')