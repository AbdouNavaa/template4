from django.urls import include, path

from . import views


app_name='template4'

urlpatterns = [
    path('projects',views.projects , name='projects'),
    path('courses',views.courses , name='courses'),
    path('files',views.files , name='files'),
    path('freinds',views.freinds , name='freinds'),
    
    path('add_project',views.add_project , name='add_project'),
    path('add_course<int:id>',views.add_course , name='add_course'),
    path('add_skill<int:id>',views.add_skill , name='add_skill'),
    path('add_file<int:id>',views.add_file , name='add_file'),
    path('add_activity<int:id>',views.add_activity , name='add_activity'),
    path('add_freind<int:id>',views.add_freind , name='add_freind'),
    
    path('delete_freind<int:id>',views.delete_freind , name='delete_freind'),
    
]