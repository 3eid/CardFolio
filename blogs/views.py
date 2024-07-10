from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from profiles.models import Profile
import json


from django.http import Http404

@login_required
def user_articles(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.user.id != profile.user.id:
        return redirect('home')  # or show a 403 error

    articles = Article.objects.filter(profile=profile)

    if 'new_article' in request.GET:
        # Check if the current article is empty and delete if true
        current_article = articles.last()
        if current_article and not current_article.heading and not current_article.subheading and not current_article.description:
            current_article.delete()

        new_article = Article(profile=profile)
        new_article.save()
        return redirect(f'/articles/user/{profile_id}/articles/?article_id={new_article.id}')
    
    article_id = request.GET.get('article_id')
    if article_id:
        try:
            article = Article.objects.get(pk=article_id, profile=profile)
        except Article.DoesNotExist:
            raise Http404("Article does not exist for the given profile")
    else:
        article = Article(profile=profile)
        article.save()

    if request.method == 'POST':
        if 'save' in request.POST:
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.instance.profile = profile
                form.save()
                return redirect(f'/articles/user/{profile_id}/articles/?article_id={article.id}')
        elif 'delete' in request.POST:
            article.delete()
            return redirect(f'/articles/user/{profile_id}/articles/')
    else:
        form = ArticleForm(instance=article)

    articles_data = list(articles.values('id', 'heading', 'subheading', 'description', 'image'))
    current_article_index = articles.filter(id__lte=article.id).count()
    articles_count = articles.count()

    return render(request, 'blogs/user_articles.html', {
        'profile': profile,
        'articles': articles,
        'form': form,
        'articles_json': json.dumps(articles_data),
        'current_article_id': article.id,
        'current_article_index': current_article_index,
        'articles_count': articles_count,
    })



    
def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    profile = get_object_or_404(Profile, user=article.profile.user)

    return render(request, 'blogs/view_article.html', {
        'article': article,
        'profile': profile,
    })
