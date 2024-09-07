from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.utils.text import slugify
# Create your models here.

Gender = (
    ('Male','Male'),
    ('woman','woman'),
)
class Developper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # lang = models.ManyToManyField('Language', related_name='skills')
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='profile/',null=True,blank=True)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=15 , choices=Gender)
    email = models.EmailField(max_length=50)
    date_birth = models.DateField(auto_now=False, auto_now_add=False)
    mobile= models.IntegerField()
    years_exper = models.FloatField()
    
    level = models.IntegerField(default=1)
    ratings = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, null=True)
        
    def save(self,*args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Developper,self).save(*args, **kwargs)
    def __str__(self):
        return self.user.username        
        
class Friend(models.Model):
    user = models.OneToOneField(Developper, on_delete=models.CASCADE)
    friends = models.ManyToManyField(Developper, related_name='friends')
    def __str__(self):
        return self.user.user.username

from django.core.exceptions import ValidationError

class Job(models.Model):
    name = models.CharField(max_length=50, )
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name


        
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Job,self).save(*args, **kwargs)


class Categorie(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Categorie,self).save(*args, **kwargs)

class Language(models.Model):
    name = models.CharField(max_length=30)
    dev = models.ForeignKey(Developper, on_delete=models.CASCADE)
    categ = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Language,self).save(*args, **kwargs)

class Activity(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(Developper, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='profile/',null=True,blank=True)
    description = models.CharField(max_length=50, default='')
    time = models.TimeField()
    date = models.DateField(auto_now_add=False)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Activity,self).save(*args, **kwargs)

class Project(models.Model):
    name = models.CharField(max_length=50,unique=True)
    end = models.DateField(auto_now_add=False)
    description = models.CharField(max_length=100, default='')
    team = models.ManyToManyField(Developper, related_name='team')
    categories = models.ManyToManyField(Categorie, related_name='categories')
    client = models.CharField(max_length=50, default='')
    
    progress = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
        
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Project,self).save(*args, **kwargs)
        

class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Developper, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    image  = models.ImageField(upload_to='profile/',null=True,blank=True)
    views = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

        
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Course,self).save(*args, **kwargs)        
        
class File(models.Model):
    name = models.CharField(max_length=50,unique=True)
    creater = models.ForeignKey(Developper,on_delete=models.CASCADE)
    
    upload_at = models.DateTimeField(auto_now_add=True)
    size = models.FloatField()
    image  = models.FileField(upload_to='profile/', max_length=100,null=True,blank=True)
    
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

        
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(File,self).save(*args, **kwargs)    