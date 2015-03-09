from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from blog.models.entry import Entry
from blog.models.tag import Tag

class EntryAdmin(MarkdownModelAdmin):
	list_display = ("title", "created")
	prepopulated_fields = { "slug" : ("title",) }

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)