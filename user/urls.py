from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 

urlpatterns = [
   path('',views.usersignupView,name='usersignup'),
   path('register/',views.registerView,name='register'),
   path('mainpage/',views.mainpage,name="mainpage"),
   path('invalidcredentials/',views.invalidcredentials,name="invalidcredentials"),
   path('details_video/<int:id>',views.details_video_View, name='details_video'),
   path('aboutus/',views.aboutusView,name='aboutus'),
   path('contact/',views.contactView,name='contact'),
   re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
