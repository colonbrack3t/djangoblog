from django.contrib import admin

from CV.models import CV_Entry
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CV_Entry)
