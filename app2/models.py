from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

names=[
        ('001','pavi'),
        ('002','thooriga'),
        ('jingly','003'),
        ('pavithra','jingly'),
        ('dinesh','dinu'),
        ('sofi','gopi')
]

def Validate_chennai(value):
    if "chennai" in value:
        return value
    elif "india" in value:
        return value
    else:
        raise ValidationError("chennai is my place")

class Post(models.Model):
     name=models.CharField(max_length=100)
     address=models.CharField(max_length=100)
     def __str__(self):
         return self.name


class Book(models.Model):
    book_name=models.CharField(max_length=200,choices=names)
    author_name=models.CharField(max_length=200,choices=names)
    comments=models.CharField(max_length=200,blank=True,null=True)
    place=models.CharField(max_length=200,default="delhi")
    review=models.CharField(max_length=100,null=True,blank=True)
    present=models.BooleanField(null=True)
    student_date=models.DateTimeField(default=timezone.now())
    phnum=models.BigIntegerField(null=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    Student_updated=models.DateTimeField(auto_now=True,null=True)
    email=models.EmailField(default="pavi@gmail.com")
    address=models.CharField(max_length=250,validators=[Validate_chennai])
    profile_pic=models.ImageField(upload_to="images/%y/%m/%d",null=True)
    resume=models.FileField(upload_to="userfile/%y/%m/%d",null=True)
    rating=models.TextField(null=True,blank=True,help_text="pls fill rating starting from 5")

    def save(self,*args,**kwargs):
        if not self.rating:
            self.rating="fivestar"
        super(Book,self).save(*args,**kwargs)

    def __str__(self):
        return self.book_name


#one to one
class employee(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_a=models.CharField(max_length=100)
    def __str__(self):
        return self.emp_name
class salary(models.Model):
    employee=models.OneToOneField(employee,on_delete=models.CASCADE)
    salary=models.BigIntegerField()
    #def __int__(self):
       #return self.salary


#one to many
class author(models.Model):
    author_name=models.CharField(max_length=200)
    author_lang=models.CharField(max_length=200)
    def __str__(self):
        return self.author_name
class novel(models.Model):
    novel=models.ForeignKey(author,on_delete=models.CASCADE)
    novel_name=models.CharField(max_length=200)
    def __str__(self):
        return self.novel_name

#many to many
class member(models.Model):
    mem_name=models.CharField(max_length=200)
    def __str__(self):
        return self.mem_name
class club(models.Model):
    members=models.ManyToManyField(member)
    club_name=models.CharField(max_length=200)
    def __str__(self):
        return self.club_name










#



# Create your models here.


# Create your models here.
# Create your models here.
