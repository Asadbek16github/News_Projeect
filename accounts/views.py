from django.shortcuts import render
from .forms import userRegistrationform
# Create your views here.
def dashboard(request):
    user = request.user

    context = {
        'user': user
    }

    return render(request, 'registration/dashboard.html', context)

def signUp(request):
    if request.method == "POST":
        user_form = userRegistrationform(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            print(user_form.cleaned_data)

            return render(request, 'registration/signUpDone.html', {'new_user':new_user})
    else:
        user_form = userRegistrationform()
    return render(request, 'registration/signUp.html', {'user_form':user_form})
