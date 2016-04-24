from django.db import models
from django.core.urlresolvers import reverse


class Book(models.Model):
	accno = models.IntegerField(primary_key=True)
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	publication = models.CharField(max_length=50)
	edition = models.CharField(max_length=50)
	no_of_copies = models.IntegerField()
	volume = models.CharField(max_length=50)
	date_purchase = models.DateField()
	price = models.FloatField()
	status = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book_detail', kwargs={'pk':self.pk})



class Student(models.Model):
	name = models.CharField(max_length=50)
	regno = models.IntegerField()
	date_of_issue = models.DateField()
	address = models.TextField()
	course = models.CharField(
		max_length=10, 
		choices = (
			('BCA', 'BCA'), 
			('BBA', 'BBA'), 
			('MBA', 'MBA'), 
			('B.Com', 'B.Com')
		)
	)
	accno = models.ForeignKey(Book)
	gender = models.CharField(
		max_length=1, 
		choices = (
			('M', 'Male'),
			('F', 'Female')
		)
	)

	def __str__(self):
		return self.name



	def get_absolute_url(self):
		return reverse('stu_detail', kwargs={'pk':self.pk})





class Issue(models.Model):
	regno = models.ForeignKey(Student)
	accno = models.ForeignKey(Book)
	date_of_issue = models.DateField()

	def get_absolute_url(self):
		return reverse('issue_detail', kwargs={'pk':self.pk})


	#on_delete=models.CASCADE)


class Return(models.Model):
	regno = models.ForeignKey(Student)
	accno = models.ForeignKey(Book)	
	date_of_return = models.DateField()


	def get_absolute_url(self):
		return reverse('return_detail', kwargs={'pk':self.pk})


class Fine(models.Model):
	regno = models.ForeignKey(Student)
	accno = models.ForeignKey(Book)
	fine = models.FloatField()

	def get_absolute_url(self):
		return reverse('fine_detail', kwargs={'pk':self.pk})




