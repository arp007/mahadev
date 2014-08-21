from django.contrib import admin
from mahadev.models import Episode, Series, SeriesSequence

class EpisodeAdmin(admin.ModelAdmin):
	list_display = ['name', 'date']

admin.site.register(Episode, EpisodeAdmin)

class SeriesAdmin(admin.ModelAdmin):
	list_display = ['link', 'date']
admin.site.register(Series, SeriesAdmin)

class SeriesSequenceAdmin(admin.ModelAdmin):
	list_display = ['seq_num', 'crt_dt']

admin.site.register(SeriesSequence, SeriesSequenceAdmin)