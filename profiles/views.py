from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from projects.models import Project
from blogs.models import Article
from chatbot.models import Chatbot
 
from .forms import ProfileForm

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .conf import groq_api_key
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq



@csrf_exempt
def chatbot_api(request, profile_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message')
        previous_messages = data.get('prev_messages')

        chatbot_settings = Chatbot.objects.get(profile=profile_id)
        user_faqs = chatbot_settings.faq
        user_about_me = chatbot_settings.about_me
        user_work_examples = chatbot_settings.work_examples
        user_schedule = chatbot_settings.schedule

        # Create a better prompt by structuring the context and the user's message
        context = (
            f"Profile Information:\n"
            f"FAQ: {user_faqs}\n"
            f"About Me: {user_about_me}\n"
            f"Work Examples: {user_work_examples}\n"
            f"Schedule: {user_schedule}\n"
            f"\nPrevious Conversation:\n{previous_messages}\n"
            f"\nUser's Query: {user_input}\n"
            f"Respond to the user's query in a helpful and professional manner based on the profile information provided. You may not use all the information, just use the needed information only."
        )

        chat = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")
        system = "You are a Personalized chatBot assistant based on the profile information. you may not need all the profile information. answer based on the context only. if visitors send you something like 'hello' respond with 'hello, how can I help you. I am a personalized assistance for this profile owner' the response shouldn't exceed 50 words."
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        chain = prompt | chat

        llm_response = chain.invoke({"text": context}).content

        response = {"response": llm_response}
        return JsonResponse(response)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form, 'profile':profile})

@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    return redirect('view_profile', profile.id)


def view_profile(request,id):
    profile = Profile.objects.get(pk = id)
    return redirect("view_profile_chatbot", profile.id)


def view_profile_projects(request, id):
    profile = get_object_or_404(Profile, pk=id)
    projects = Project.objects.filter(profile=profile)
    return render(request, 'profiles/view_profile_projects.html', {'profile': profile, 'projects': projects})

def view_profile_articles(request,id):
    profile = get_object_or_404(Profile, pk=id)
    articles = Article.objects.filter(profile=profile)
    
    return render(request, 'profiles/view_profile_articles.html', {'profile': profile, 'articles': articles})

def view_profile_chatbot(request,id):
    profile = get_object_or_404(Profile, pk=id)
    chatbot_settings = Chatbot.objects.get(profile=profile)
    return render(request, 'profiles/view_profile_chatbot.html', {'profile': profile, })

