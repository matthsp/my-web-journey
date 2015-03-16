# -*- coding: utf-8 -*-
from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models.entry import Entry 
from blog.models.entry import EntryQuerySet 

class IndexAction(generic.View):
	
	page = None
	paginate_by = 1
	# Indexes before and after the current page to display
	page_interval = 3
	# Blog entries
	entries = None

	template_name = "home.html"

	# @function get the home page - GET METHOD
	# @param self
	# @param request
	# @param page the page to display (default = 1)
	def get(self, request, page = 1): 
		
		search = None;
		# If "search" is defined : Filter the list of entries 
		if request.GET.get("search", "").strip() != "":
			search = request.GET.get("search")
			entry_list = Entry.objects.search( search )
		# Else : Get the list of entries published
		else:
			entry_list = Entry.objects.published()

		# Get the paginator for the list of entries
		paginator = Paginator(entry_list, self.paginate_by) 

		# If self.page is not set, get it from the request
		if self.page == None:
			self.page = int(self.kwargs['page'])
		try:
			# "page" value must be at least 1
			if int(self.page) <= 0:
				self.page = 1
			# Get the list of entries for the target page
			entries = paginator.page(self.page)
		
		except PageNotAnInteger:
			# If page is not an integer, page may be not defined
			# We use a default value : 1 (first page)
			self.page = 1
			# Get the list of entries for the first page
			entries = paginator.page(self.page)
		
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			entries = paginator.page(paginator.num_pages)

		self.entries = entries

		page_range = entries.paginator.page_range
		
		# We get the index of the current page
		current_index = self.page -1
		# Then we create the first and last index based on current_index and the paginate_interval
		first_index = current_index - self.page_interval
		last_index = current_index + self.page_interval
		if first_index < 0:
			first_index = 0
		if last_index >= paginator.num_pages:
			last_index = paginator.num_pages -1
		
		# If the number of pages is superior to the pages_interval
		if (last_index < entries.paginator.num_pages - 1) or (first_index > 0):
			# Truncate the page_range
			page_range = page_range[first_index:last_index]

		return render(request, self.template_name, {'entries': self.entries, 'page_range': page_range, 'page': self.page, 'search' : search, } )


class DetailAction(generic.DetailView):
	model = Entry
	template_name = "article.html"
