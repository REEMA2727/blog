from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add/', views.add_blog, name='add_blog'),

    path(
        'detail/<int:id>/',
        views.detail,
        name='detail'
    ),

    path(
        'update/<int:id>/',
        views.update_blog,
        name='update'
    ),

    path(
        'delete/<int:id>/',
        views.delete_blog,
        name='delete'
    ),

    path(
        'add-category/',
        views.add_category,
        name='add_category'
    ),

    path(
        'categories/',
        views.category_list,
        name='categories'
    ),

    path(
        'category/<int:id>/',
        views.blogs_by_category,
        name='category_blogs'
    ),

    path(
        'delete-category/<int:id>/',
        views.delete_category,
        name='delete_category'
    ),

    path('like/<int:blog_id>/', views.like_blog, name='like_blog'),

    path(
        'liked/',
        views.liked_blogs,
        name='liked'
    ),

    path(
        'unlike/<int:id>/',
        views.unlike_blog,
        name='unlike'
    ),

    path(
        'add-author/',
        views.add_author,
        name='add_author'
    ),
]

# Media files (images)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )