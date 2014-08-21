from django.db import models
from datetime import datetime

'''
AbstractBase class is a base class for all the models
'''
class AbstractBase(models.Model):
    class Meta:
    	abstract = True

    crt_dt = models.DateTimeField(default=datetime.now())
    upd_dt = models.DateTimeField(blank=True, null=True)

'''
Episode class will be responsible for storing Episode object
'''
class Episode(AbstractBase):
    name = models.CharField(max_length=50)
    date = models.DateField()
    link = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)


'''
Series class will contain list of series
'''
class Series(AbstractBase):
    class Meta:
        ordering = ['-date']

    link = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField()
    thumbnail_url = models.CharField(max_length=200)
    episode = models.ForeignKey(Episode)

'''
SeriesSequence class will contain list of series in sequence
'''
class SeriesSequence(AbstractBase):
    link = models.CharField(max_length=200, blank=True, null=True)
    iframe_link = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=50)
    thumbnail_url = models.CharField(max_length=200)
    seq_num = models.IntegerField()
    series = models.ForeignKey(Series)
    

