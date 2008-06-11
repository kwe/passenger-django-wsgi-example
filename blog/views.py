from wally.blog.models import Article
from django.shortcuts import render_to_response

def blog_index(request):
	"""Display the homepage"""
	e = Article.objects.all()
	return render_to_response('blog_index.html', {'latest_articles': e})
