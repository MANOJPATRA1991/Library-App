"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin

# Use include() to add URLS from the catalog application
from django.conf.urls import include

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Maps all urls with the pattern admin/ to the module admin.site.urls
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    # Maps all urls with the pattern catalog/ to the module catalog.urls
    # the file with the relative URL /catalog/urls.py
    url(r'^catalog/', include('catalog.urls')),
]

urlpatterns += [
    # Redirect empty url to /catalog/
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Enable serving of static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)