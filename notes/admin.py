from django.contrib import admin
from .models import Tag, Note

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)
admin.site.register(Note, NoteAdmin)
