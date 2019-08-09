from django.urls import path

from . import views

app_name='reporters'
urlpatterns = [
    path('<int:reporter_id>/', views.ArticleListView.as_view(), name='reporter_articles'),
    path('new/', views.new_reporter, name='new_reporter'),
]
