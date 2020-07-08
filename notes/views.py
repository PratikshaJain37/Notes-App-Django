from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Note
from .forms import NoteModelForm

# Create your views here.

class NoteCreateView(CreateView):
    template_name = 'notes/note_create.html'
    form_class = NoteModelForm
    queryset = Note.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    # success_url = /

class NoteListView(ListView):
    template_name = 'notes/note_list.html'
    queryset = Note.objects.all()


class NoteDetailView(DetailView):
    template_name = 'notes/note_detail.html'
    queryset = Note.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Note, id=id_)


class NoteUpdateView(UpdateView):
    template_name = 'notes/note_create.html'
    form_class = NoteModelForm
    queryset = Note.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Note, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class NoteDeleteView(DeleteView):
    template_name = 'notes/note_delete.html'
 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Note, id=id_)
   
    def get_success_url(self):
        return reverse('notes:note-list')