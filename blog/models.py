from django.db import models

class Article(models.Model):
	"""An Article model"""
	title = models.CharField('Title', max_length=40)
	body = models.TextField('Article Body')
	
	def __unicode__(self):
		"""return something valid"""
		return self.title
		
	class Admin:
		fields = (
			(None, {'fields':('title','body')}),
		)
		list_display = ('title', 'body')
	class Meta:
		ordering = ['title']
