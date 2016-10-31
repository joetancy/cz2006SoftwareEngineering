"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from home import views as homeView
from register import views as accountView
from listings import views as listingsView

urlpatterns = [
    url(r'^$', homeView.index, name='index'),

    url(r'^account/register', accountView.register, name='accountRegistration'),
    url(r'^account/login', accountView.login, name='accountLogin'),
    url(r'^account/logout', accountView.logout, name='accountLogout'),

    url(r'^listing/create/$', listingsView.create, name='createListing'),
    url(r'^listing/update/(?P<listing_id>[0-9]+)$',
        listingsView.update, name='updateListing'),
    url(r'^listing/view/$', listingsView.view, name='viewListing'),
    url(r'^listing/viewAll/$', listingsView.viewAll, name='viewAllListing'),
    url(r'^listing/view/(?P<listing_id>[0-9]+)$',
        listingsView.viewDetail, name='viewListingDetails'),
    url(r'^listing/delete/(?P<listing_id>[0-9]+)$',
        listingsView.delete, name='deleteListing'),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
