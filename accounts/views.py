from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import userRegistrationform, profileModelUpdateForm, userModelUpdateForm
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import Profile
# Create your views here.
def dashboard(request):
    user = request.user

    context = {
        'user': user
    }

    return render(request, 'registration/dashboard.html', context)

# Funcsiyaga asoslangan sign up view
def signUp(request):
    if request.method == "POST":
        user_form = userRegistrationform(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/signUpDone.html', {'new_user':new_user})
    else:
        user_form = userRegistrationform()
    return render(request, 'registration/signUp.html', {'user_form':user_form})


# class ga asoslangan sign up view
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login_page')
    template_name = 'registration/signUp.html'

def updateUserAndProfileModelView(request):
    if request.method == "POST":
        user_form = userModelUpdateForm(instance=request.user, data=request.POST)
        profile_form = profileModelUpdateForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = userModelUpdateForm(instance=request.user)
        profile_form = profileModelUpdateForm(instance=request.user.profile)
    
    return render(request, 'registration/UpdateModels.html', {'user_form':user_form, 'profile_form':profile_form})