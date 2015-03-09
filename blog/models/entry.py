from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse

from .tag import Tag 

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class Entry(models.Model):
	# attributes of an entry
	title = models.CharField(max_length=200)
	body = MarkdownField()
	slug = models.SlugField(max_length=75, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True) 
	modified = models.DateTimeField(auto_now=True)

	# linked tags of an entry
	tags = models.ManyToManyField(Tag)

	objects = EntryQuerySet.as_manager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article_detail", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Blog entry"
		verbose_name_plural = "Blog entries"
		ordering = ["-created"]
		app_label = "blog"
