# -*- coding: utf-8 -*-
from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models.entry import Entry 

class IndexAction(generic.View):
	
	page = None
	paginate_by = 3
	# indexes before and after the current page to display
	paginate_range = 5

	template_name = "home.html"

	def get(self, request, page = 1) : 
		entry_list = Entry.objects.all()
		paginator = Paginator(entry_list, self.paginate_by) 

		if self.page == None :
			self.page = int(self.kwargs['page'])

		try:
			if int(self.page) <= 0:
				self.page = 1

			entries = paginator.page(self.page)
		except PageNotAnInteger:
			self.page = 1
			# If page is not an integer, deliver first page.
			entries = paginator.page(self.page)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			entries = paginator.page(paginator.num_pages)

		# first index to show in the paginator on the bottom of the page
		first_index = int(self.page);
		
		if first_index < 5:
			first_index = 1
		else:
			first_index = first_index-self.paginate_range;
	
		# last index to show in the paginator on the bottom of the page
		last_index = int(self.page) + self.paginate_range;
		if last_index + 1 > paginator.num_pages:
			last_index = paginator.num_pages

		page_range = entries.paginator.page_range
		debug_range = page_range
		page_range = page_range[first_index-1: last_index]

		return render(request, self.template_name, {'entries': entries, 'page_range': page_range, 'page': self.page })


class DetailAction(generic.DetailView):
	model = Entry
	template_name = "article.html"
