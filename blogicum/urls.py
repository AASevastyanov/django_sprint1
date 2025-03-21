from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        include(
            'blogicum.blog.urls',
            namespace='blog')),
    path(
        'pages/',
        include(
            'blogicum.pages.urls',
            namespace='pages')),
]
