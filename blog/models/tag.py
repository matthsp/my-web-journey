from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse

class Tag(models.Model):
	slug = models.SlugField(max_length=75, unique=True)

	def __str__(self):
		return self.slug

	class Meta:
		verbose_name = "Tag entry"
		verbose_name_plural = "Tag entries"
		app_label = "blog"

# TODO :  add some queries for popular tags, etc.
# class TagQuerySet(models.QuerySet):
	