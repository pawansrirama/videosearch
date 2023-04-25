from django.urls import path,re_path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 

urlpatterns = [
   path('admin/adminLogin/',v.adminLoginView,name='adminLogin'),
   path('admin/adminmainpage/',v.adminmainpageView,name="adminmainpage"),
   path('admin/invalidcredentials1/',v.invalidcredentials1,name="invalidcredentials1"),
   path('admin/completed/',v.completed,name="completed"),
   re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}) 
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
