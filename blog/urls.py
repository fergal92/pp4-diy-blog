from django.urls import path
from . import views

# Add URL patterns
urlpatterns = [
    path("submit/", views.submit_post, name="submit_post"),
    path("", views.PostList.as_view(), name="home"),
    path("home", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
]
