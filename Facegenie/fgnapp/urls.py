from django.urls import path, include
from fgnapp import views
from django.contrib import admin
from django .views.static import serve
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='fgn'),
    path('modelTrigger/',views.displaying_info_model,name='displaying_model_info'),
    path('saving_json/',views.saving_json,name = 'saving_json'),
    path('login/', views.handlelogin, name='loggingin'),
    path('trigerring/', views.Trigger,name ='Trigger' ),
    path('signup/', views.handleSignup, name='signup'),
    path('logout/', views.handlelogout, name='loggingout')
]

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$',serve,{
#             'document_root':settings.MEDIA_ROOT,
#         }),
#     ]
