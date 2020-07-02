from django.shortcuts import render, get_object_or_404
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Note

# Create your views here.

class NoteListView(ListView):
    template_name = 'notes/note_list.html'
    queryset = Note.objects.all()


class NoteDetailView(DetailView):
    template_name = 'notes/note_detail.html'
    queryset = Note.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Note, id=id_)
