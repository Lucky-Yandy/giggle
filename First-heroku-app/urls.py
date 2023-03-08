from django.urls import path

import views

urlpatterns = [
    path('', views.homepage),
    path('search-results/', views.search_results),
    path('giggle-news/', views.giggle_news),
]

# Boilerplate to include static files.
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static('static/', document_root=settings.STATIC_ROOT)

