from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticlHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ArticleCategory.as_view(), name='categ'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', insite, name='login')
]
