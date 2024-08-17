from django.shortcuts import render,redirect,get_object_or_404
from gym_function.models import gym_members
from .forms import RegisterFormMember,UpdateFormMember
import mysql.connector

# Create your views here.

def showMember_views(request):
    members = gym_members.objects.all()  # Fetch all members
    return render(request, 'index.html', {"members": members})


from django.shortcuts import render, redirect
from django.db import connection

def updateMember_views(request):
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


def addMember_views(request):
    if request.method == 'POST':
        form = RegisterFormMember(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/member?page=1')
    else:
        form = RegisterFormMember()
    return render(request,'member/add_member.html',{'form':form})


