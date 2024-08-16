from django.shortcuts import render,redirect
from gym_function.models import gym_members
from .forms import RegisterFormMember
from django.core.paginator import Paginator

# Create your views here.

def showMember_views(request):


    members = gym_members.objects.all()  # Fetch all members

    paginator = Paginator(members,10)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {"page_obj": page_obj})


def addMember_views(request):
    if request.method == 'POST':
        form = RegisterFormMember(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/member?page=1')
    else:
        form = RegisterFormMember()
    return render(request,'add_member.html',{'form':form})