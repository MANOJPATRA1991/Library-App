from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    # This view will be implemented as a Class.
    # as_view() does all the work of creating an
    # instance of the class, and making sure that
    # the right handler methods are called for incoming HTTP requests
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    # book-detail url mapper
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name="book-detail"),
    # authors url mapper
    url(r'^authors/$', views.AuthorListView.as_view(), name="authors"),
    # author-detail url mapper
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name="author-detail"),
]