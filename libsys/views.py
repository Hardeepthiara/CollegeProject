from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libsys.models import Student, Book, Issue, Fine, Return
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#from crispy_forms.helper import FormHelper




#from django.http import HttpResponse

def index(request):
	return render(request, 'libsys/index.html')

def contact(request):
	return render(request, 'libsys/contact.html')

def service(request):
	return render(request, 'libsys/service.html')

def about(request):
	return render(request, 'libsys/about.html')

#Students

class StuList(ListView):
	template_name = "libsys/stu_list.html"
	model=Student

class  StuDetail(DetailView):
	template_name = "libsys/stu_detail.html"
	model=Student

class  StuCreate(LoginRequiredMixin, CreateView):
	model=Student
	template_name = "libsys/stu_form.html"
	
	fields=['name', 'regno',  'date_of_issue', 'address', 'course', 'accno', 'gender']

class  StuUpdate(LoginRequiredMixin, UpdateView):
	model=Student
	template_name = "libsys/stu_form.html"
	fields=['name', 'regno', 'date_of_issue', 'address', 'course', 'accno', 'gender']

class  StuDelete(LoginRequiredMixin, DeleteView):
	model=Student
	template_name = "libsys/stu_list.html"
	success_url = reverse_lazy('stu_list')







#Books

class Books(ListView):
	template_name = "libsys/books.html"
	model=Book

class  BookDetail(DetailView):
	template_name = "libsys/book_detail.html"
	model=Book

class  BookCreate(LoginRequiredMixin, CreateView):
	model=Book
	template_name = "libsys/book_form.html"
	fields=['accno', 'author', 'title', 'publication', 'edition', 'no_of_copies', 'volume', 'date_purchase', 'price', 'status']

class  BookUpdate(LoginRequiredMixin, UpdateView):
	model=Book
	template_name = "libsys/book_form.html"
	fields=['accno', 'author', 'title', 'publication', 'edition', 'no_of_copies', 'volume', 'date_purchase', 'price', 'status']

class  BookDelete(LoginRequiredMixin, DeleteView):
	model=Book
	success_url= reverse_lazy('books')
	template_name = "libsys/books.html"

#Issue

class Issue1(ListView):
	template_name = "libsys/issue.html"
	model=Issue

class IssueDetail(DetailView):
	template_name = "libsys/issue_detail.html"
	model=Issue

class  IssueCreate(LoginRequiredMixin, CreateView):
	model=Issue
	template_name = "libsys/issue_form.html"
	fields=['regno', 'accno', 'date_of_issue']

class  IssueUpdate(LoginRequiredMixin, UpdateView):
	model=Issue
	template_name = "libsys/issue_form.html"
	fields=['regno', 'accno', 'date_of_issue']

class  IssueDelete(LoginRequiredMixin, DeleteView):
	model=Issue
	template_name = "libsys/issue.html"
	success_url= reverse_lazy('issue')


#Fineeee

class Fine1(ListView):
	template_name = "libsys/fine.html"
	model=Fine

class  FineDetail(DetailView):
	template_name = "libsys/fine_detail.html"
	model=Fine

class  FineCreate(LoginRequiredMixin, CreateView):
	model=Fine
	template_name = "libsys/fine_form.html"
	fields=['regno', 'accno', 'fine']

class  FineUpdate(LoginRequiredMixin, UpdateView):
	model=Fine
	template_name = "libsys/fine_form.html"
	fields=['regno', 'accno', 'fine']

class  FineDelete(LoginRequiredMixin, DeleteView):
	model=Fine
	success_url= reverse_lazy('fine')
	template_name = "libsys/fine.html"


#return

class Return1(ListView):
	template_name = "libsys/return.html"
	model=Return

class  ReturnDetail(DetailView):
	template_name = "libsys/return_detail.html"
	model=Return

class  ReturnCreate(LoginRequiredMixin, CreateView):
	model=Return
	template_name = "libsys/return_form.html"
	fields=['regno', 'accno', 'date_of_return']

class  ReturnUpdate(LoginRequiredMixin, UpdateView):
	model=Return
	template_name = "libsys/return_form.html"
	fields=['regno', 'accno', 'date_of_return']

class  ReturnDelete(LoginRequiredMixin, DeleteView):
	model=Return
	success_url= reverse_lazy('return')
	template_name = "libsys/return.html"






@login_required
def submit_session(request):
 	return render(request, 'libsys/submit_session.html')





