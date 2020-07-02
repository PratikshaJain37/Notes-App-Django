from django.urls import path
from .views import (
    NoteDetailView,
    NoteListView
)

app_name = 'notes'

urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('<int:id>/', NoteDetailView.as_view(), name='note-detail')
]