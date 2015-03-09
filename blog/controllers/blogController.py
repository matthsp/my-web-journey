# -*- coding: utf-8 -*-
from django.views import generic
from blog.models.entry import Entry 

class IndexAction(generic.ListView):
	queryset = Entry.objects.published()
	template_name = "home.html"
	# custom vars (used inside the view)
	paginate_by = 5

class DetailAction(generic.DetailView):
	model = Entry
	template_name = "article.html"
