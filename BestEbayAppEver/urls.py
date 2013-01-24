from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'BestEbayAppEver.ProductFinder.views.home', name='home'),
     url(r'^searchResults', 'BestEbayAppEver.ProductFinder.views.searchResults', name='searchResults'),
     url(r'^search', 'BestEbayAppEver.ProductFinder.views.search', name='search'),
     url(r'^configs', 'BestEbayAppEver.ProductFinder.views.configs', name='configs'),
     url(r'^modifyConfigs', 'BestEbayAppEver.ProductFinder.views.modifyConfigs', name='modifyConfigs'),
    # url(r'^BestEbayAppEver/', include('BestEbayAppEver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
