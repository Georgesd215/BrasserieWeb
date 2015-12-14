from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', "BrasserieSite.views.index", name='index'),
    url(r'^NosBiere/', "BrasserieSite.views.NosBiere", name='NosBiere'),
    url(r'^accounts/profile/', "BrasserieSite.views.profile", name='profile'),
    url(r'^BARBANE_DEMENTHE/$', "BrasserieSite.views.BARBANE_DEMENTHE", name='BARBANE_DEMENTHE'),
    url(r'^BARBANE_FLORALE/$', "BrasserieSite.views.BARBANE_FLORALE", name='BARBANE_FLORALE'),
    url(r'^BARBANE_BLONDE/$', "BrasserieSite.views.BARBANE_BLONDE", name='BARBANE_BLONDE'),
    url(r'^BARBANE_NOEL/$', "BrasserieSite.views.BARBANE_NOEL", name='BARBANE_NOEL'),
    url(r'^BARBANE_MONDIALE/$', "BrasserieSite.views.BARBANE_MONDIALE", name='BARBANE_MONDIALE'),
    url(r'^BARBANE_DANS_LES_VIGNES/$', "BrasserieSite.views.BARBANE_DANS_LES_VIGNES", name='BARBANE_DANS_LES_VIGNES'),
        
    # url(r'^BrasserieSite/', include('BrasserieSite.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

