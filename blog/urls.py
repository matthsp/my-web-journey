from django.conf.urls import patterns, url
from blog.controllers import feedController, blogController

urlpatterns = patterns(
	'',
    url(r'^feed/', feedController.IndexAction, name="feed"),
    url(r'^$', blogController.IndexAction.as_view(page=1), name="home"),
    url(r'^page/(?P<page>\d+)$', blogController.IndexAction.as_view(), name="page"),
    url(r'^(?P<slug>\S+)$', blogController.DetailAction.as_view(), name="article_detail"),
)

