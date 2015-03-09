# -*- coding: utf-8 -*-
from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models.entry import Entry 

class IndexAction(generic.View):
	
	page = None
	paginate_by = 3
	
	template_name = "home.html"

	def get(self, request, page = 1) : 
		entry_list = Entry.objects.all()
		paginator = Paginator(entry_list, self.paginate_by) 

		if self.page == None :
			self.page = self.kwargs['page']

		try:
			entries = paginator.page(self.page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			entries = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			entries = paginator.page(paginator.num_pages)

		return render(request, self.template_name, {'entries': entries})


class DetailAction(generic.DetailView):
	model = Entry
	template_name = "article.html"
