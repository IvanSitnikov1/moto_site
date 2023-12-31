from django.urls import path, include

from .views import *

urlpatterns = [
    path('', MotorcycleHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('post/delete/<slug:post_slug>', delete, name='delete'),
    path('post/update/<slug:post_slug>', UpdatePost.as_view(), name='update'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path(
        'category/<slug:cat_slug>/',
        MotorcycleCategory.as_view(),
        name='category'
    ),
    path('social/', include('social_django.urls', namespace='social_django')),
]
