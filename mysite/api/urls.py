from django.urls import path
from . import views

urlpatterns = [
    path("blogposts", views.BlogListCreate.as_view(), name="blogpost-view"),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="blogpost-update"),
]