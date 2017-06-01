from . import views,api
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', views.root_index, name="root_index"),
    url(r'^login$', views.root_login, name="root_login"),
    url(r'^logout$', views.root_logout, name="root_logout"),
    url(r'^article$', views.root_article_list, name="root_article_list"),
    url(r'^article/write/html$', TemplateView.as_view(template_name="article_write.html"), name="article_write_html"),
    url(r'^article/write/markdown$', TemplateView.as_view(template_name="article_markdown.html"), name="article_markdown"),
    url(r'^article/(?P<id>\d+)$', views.root_article_editor, name="root_article_editor"),
    url(r'^api/article([/]?)(?P<id>\d*)$', login_required(api.ArticleApi.as_view())),
]
