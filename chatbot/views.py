from django.shortcuts import render, redirect, get_object_or_404
from .models import Chatbot
from profiles.models import Profile
from .forms import ChatbotForm

def update_chatbot(request, profile_no):
    profile = get_object_or_404(Profile, id=profile_no)
    chatbot, created = Chatbot.objects.get_or_create(profile=profile)

    if request.method == 'POST':
        form = ChatbotForm(request.POST, instance=chatbot)
        if form.is_valid():
            form.save()
            return redirect('update_chatbot', profile_no=profile_no)
    else:
        form = ChatbotForm(instance=chatbot)

    return render(request, 'update_chatbot.html', {
        'form': form,
        'profile': profile,
    })
