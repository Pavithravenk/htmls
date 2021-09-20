from django.contrib import admin
from.models import Post,Book,employee,salary,author,novel,member,club
class Bookadmin(admin.ModelAdmin):

    fields=['book_name','author_name','created_date','Student_updated','new_content','email','address','profile_pic','resume','rating']
    readonly_fields=['created_date','Student_updated','new_content']
    def new_content(self,obj,*args,**kwargs):
        return str(obj.book_name)
    class Meta:
        model=Book

admin.site.register(Post)
admin.site.register(Book,Bookadmin)
admin.site.register(employee)
admin.site.register(salary)
admin.site.register(author)
admin.site.register(novel)
admin.site.register(member)
admin.site.register(club)




# Register your models here
# Register your models here.


# Register your models here.


# Register your models here.
