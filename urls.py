from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$','wally.blog.views.blog_index'),
	(r'^admin/', include('django.contrib.admin.urls')),
)
