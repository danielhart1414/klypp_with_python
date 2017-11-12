from django.shortcuts import render


# Serves up the home page
def home_page(request):
    return render(request, 'my_home.html')
