from django.contrib import admin
from libsys.models import * 






@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass
	list_display=('title', 'author',)
	search_fields=['accno', 'title']
	list_filter=('accno', 'title',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'regno','date_of_issue','date_of_issue')

class IssueAdmin(admin.ModelAdmin):
	list_display=('regno','date_of_issue',)
	search_fields=['date_of_issue']
	list_filter=('regno','accno','date_of_issue')
admin.site.register(Issue,IssueAdmin)




class ReturnAdmin(admin.ModelAdmin):
	list_display=('regno','date_of_return',)
admin.site.register(Return,ReturnAdmin)

class FineAdmin(admin.ModelAdmin):
	list_display=('regno','fine',)

admin.site.register(Fine,FineAdmin)






