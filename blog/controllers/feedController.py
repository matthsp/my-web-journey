# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from blog.models.entry import Entry 

class IndexAction(Feed):
	title = "A Web Journey - By Matthieu Pouille [pouillematthieu@gmail.com]"
	link = "/feed/"
	description = "5 latests post of my Web journey"

	def items(self):
		# return the 5 latest posts
		# TODO : change to EntryQuerySet and create the getTop(X) method
		return Entry.objects.published()[:5]