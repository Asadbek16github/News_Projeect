from django.shortcuts import render

# Create your views here.
def dashboard(request):
    user = request.user

    context = {
        'user': user
    }

    return render(request, 'registration/dashboard.html', context)