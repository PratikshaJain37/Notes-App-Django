from django.urls import path
from .views import (
    NoteCreateView,
    NoteDetailView,
    NoteListView,
    NoteUpdateView,
    NoteDeleteView,
)

app_name = 'notes'

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    #path('create/', NoteCreateView.as_view(success_url = "/notes/create/"), name='article-create'),
    path('create/', NoteCreateView.as_view()),
    path('<int:id>/', NoteDetailView.as_view(), name='note-detail'),
    path('<int:id>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('<int:id>/delete/', NoteDeleteView.as_view(), name='article-delete'),
]