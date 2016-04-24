"""libmansys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from libsys import views, auth


urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/', auth.login, name='login'),
    url(r'^logout/', auth.logout, name='logout'),
    url(r'^register/', auth.register, name='register'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^service/', views.service, name='service'),
    url(r'^about/', views.about, name='about'),

    #Students

   url(r'^student/$', views.StuList.as_view(), name='stu_list'),
   url(r'^student/(?P<pk>[0-9]+)/$', views.StuDetail.as_view(), name='stu_detail'),
   url(r'^student/create/$', views.StuCreate.as_view(), name='stu_create'),
   url(r'^student/update/(?P<pk>[0-9]+)/$', views.StuUpdate.as_view(), name='stu_update'),
   url(r'^student/delete/(?P<pk>[0-9]+)/$', views.StuDelete.as_view(), name='stu_delete'),

   #Books

   url(r'^book/$', views.Books.as_view(), name='books'),
   url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name='book_detail'),
   url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
   url(r'^book/update/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name='book_update'),
   url(r'^book/delete/(?P<pk>[0-9]+)/$', views.BookDelete.as_view(), name='book_delete'),

   #Issue of books

   url(r'^issue/$', views.Issue1.as_view(), name='issue'),
   url(r'^issue/(?P<pk>[0-9]+)/$', views.IssueDetail.as_view(), name='issue_detail'),
   url(r'^issue/create/$', views.IssueCreate.as_view(), name='issue_create'),
   url(r'^issue/update/(?P<pk>[0-9]+)/$', views.IssueUpdate.as_view(), name='issue_update'),
   url(r'^issue/delete/(?P<pk>[0-9]+)/$', views.IssueDelete.as_view(), name='issue_delete'),

  #fine of books
   url(r'^fine/$', views.Fine1.as_view(), name='fine'),
   url(r'^fine/(?P<pk>[0-9]+)/$', views.FineDetail.as_view(), name='fine_detail'),
   url(r'^fine/create/$', views.FineCreate.as_view(), name='fine_create'),
   url(r'^fine/update/(?P<pk>[0-9]+)/$', views.FineUpdate.as_view(), name='fine_update'),
   url(r'^fine/delete/(?P<pk>[0-9]+)/$', views.FineDelete.as_view(), name='fine_delete'),

   #Returns of books
   url(r'^return/$', views.Return1.as_view(), name='return'),
   url(r'^return/(?P<pk>[0-9]+)/$', views.ReturnDetail.as_view(), name='return_detail'),
   url(r'^return/create/$', views.ReturnCreate.as_view(), name='return_create'),
   url(r'^return/update/(?P<pk>[0-9]+)/$', views.ReturnUpdate.as_view(), name='return_update'),
   url(r'^return/delete/(?P<pk>[0-9]+)/$', views.ReturnDelete.as_view(), name='return_delete'),

   url(r'^submit/', views.submit_session, name='submit_session'),

)

