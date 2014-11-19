from django.conf.urls import patterns, url, include
from frontend import views
 
urlpatterns = patterns('frontend.views',
    url(r'^', 'home_page', name='home'),
)