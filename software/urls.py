"""software URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path,include

#for image_Upload
from django.conf import settings
from django.conf.urls.static import static
from scheduling import views as sc
from assigning import views as ass

#direct implementation




urlpatterns = [
    #path('',pv.index,name='index'),
    path('admin/', admin.site.urls),
    path('send/',ass.send,name = 'index'),
    path('login/', sc.login,name='ass'),
    path('', sc.notice,name='notice'),
    path("index/<int:id>", ass.index, name='profile'),
    path('selection/',ass.selection),
    
    #path('profile/', include('page.urls')),
   # path('',include('page.urls')),
    #path('register/', av.register, name="register"),
    #path('', include("django.contrib.auth.urls")),
    #path('schedule/',include('schedule.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # + staticfiles_urlpatterns()   # This line is for image upload

# handler404 = 'page.views.error_404_view'

admin.site.site_header = "Pulchowk Campus Admin"
#admin.site.site_title = "Admin"
admin.site.index_title = "Pulchowk Campus Admin Portal"