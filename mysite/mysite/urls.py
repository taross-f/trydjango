from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url( r'^helloworld/', include('helloworld.urls')),
    url(r'^myapp/', include('myapp.urls', namespace='myapp')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('helloworld.urls'))
]
