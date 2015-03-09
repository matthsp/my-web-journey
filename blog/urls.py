from django.conf.urls import patterns, url
from blog.controllers import feedController, blogController

urlpatterns = patterns(
	'',
    url(r'^feed/', feedController.IndexAction(), name="feed"),
    url(r'^$', blogController.IndexAction.as_view(), name="home"),
    url(r'^(?P<slug>\S+)$', blogController.DetailAction.as_view(), name="article_detail"),
)

