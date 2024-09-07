from django.contrib import admin

from .models import *



class DevAdmin(admin.ModelAdmin):
    list_display = ('id','user',)

admin.site.register(Developper,DevAdmin)

class FriendAdmin(admin.ModelAdmin):
    list_display = ('id','user',)

admin.site.register(Friend,FriendAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(Job,JobAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(Project,ProjectAdmin)

# course
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(Course,CourseAdmin)

# file
class FileAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(File,FileAdmin)

# lang
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(Language,LanguageAdmin)

# categ
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(Categorie,CategorieAdmin)

# activities
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(Activity,ActivityAdmin)