from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   # url(r'^$','contact.views.contact', name='contact'),
    url(r'^$', 'contact.views.add_contact', name='add_contact'),
)
                
