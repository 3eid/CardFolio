from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from profiles.models import Profile
import json

@login_required
def user_articles(request, user_id):
    if request.user.id != user_id:
        return redirect('home')  # or show a 403 error

    profile = get_object_or_404(Profile, user_id=user_id)
    articles = Article.objects.filter(profile=profile)

    if 'new_article' in request.GET:
        # Check if the current article is empty and delete if true
        if articles.exists():
            current_article = articles.last()
            if not current_article.heading and not current_article.subheading and not current_article.description:
                current_article.delete()

        new_article = Article(profile=profile)
        new_article.save()
        return redirect(f'/articles/user/{user_id}/articles/?article_id={new_article.id}')
    else:
        article_id = request.GET.get('article_id')
        article = articles.first() if article_id is None else get_object_or_404(Article, pk=article_id, profile=profile)

    if request.method == 'POST':
        if 'save' in request.POST:
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.instance.profile = profile  # Set the profile before saving
                form.save()
                return redirect(f'/articles/user/{user_id}/articles/?article_id={article.id}')
        elif 'delete' in request.POST:
            article.delete()
            return redirect(f'/articles/user/{user_id}/articles/')
    else:
        form = ArticleForm(instance=article)

    articles_data = list(articles.values('id', 'heading', 'subheading', 'description', 'image'))

    return render(request, 'blogs/user_articles.html', {
        'form': form,
        'articles_json': json.dumps(articles_data),
        'current_article_id': article.id if article else None,
    })

def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    profile = get_object_or_404(Profile, user=article.profile.user)

    return render(request, 'blogs/view_article.html', {
        'article': article,
        'profile': profile,
    })
