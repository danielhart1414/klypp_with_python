from django.shortcuts import render

from .models import KlyppUser


# A practice request
def user_list(request):
    klypp_users = KlyppUser.objects.all()
    return render(request, 'user_profiles/user_list.html', {'bob': klypp_users})
