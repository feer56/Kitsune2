from django.conf.urls.defaults import include, patterns
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^search', include('search.urls')),
    (r'^forums', include('forums.urls')),
    (r'^admin/', include(admin.site.urls)),
)

# Handle 404 and 500 errors
handler404 = 'sumo.views.handle404'
handler500 = 'sumo.views.handle500'

if settings.DEBUG:
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
          {'document_root': settings.MEDIA_ROOT}),
    )
