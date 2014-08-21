from django.http import HttpResponse
import json
from mahadev.models import Episode, Series, SeriesSequence
from django.core import serializers
from django.views.generic import View
from django.views.generic.base import TemplateView

from django.views.generic.list import ListView
from django.utils import timezone
from episodeManger import sav, savSeq, createEp
from django.template import RequestContext, loader
from django.utils import simplejson



class EpisodeListView(ListView):

    model = Episode

    def get_context_data(self, **kwargs):
        context = super(EpisodeListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
episodeList = EpisodeListView.as_view()

class SeriesListView(ListView):
    model = Series
    template_name = "series_list.html"

seriesListView = SeriesListView.as_view()



class PlaySeries(TemplateView):
    template_name = 'mahadev/seriessequence_list.html'

    def get_context_data(self, **kwargs):
        context = super(PlaySeries, self).get_context_data(**kwargs)
        seq = SeriesSequence.objects.filter(series_id=kwargs['ep_id']).order_by('seq_num')
        context['seq'] = seq
        return context
        

playSeries = PlaySeries.as_view()

class PlaySeq(View):
    

    def get(self, request, *args, **kwargs):
        data = SeriesSequence.objects.filter(series_id=kwargs['ep_id']).order_by('seq_num').filter(seq_num=int(kwargs['seq']))
        vid_link = data[0].link
        return HttpResponse(simplejson.dumps({"link":vid_link}), mimetype='application/json')
        

playSeq = PlaySeq.as_view()

    
class SaveEpisode(View):
    def post(self, request):
    	data = json.loads(request.body)
        series = sav(data)
        savSeq(data, series)
        return HttpResponse(status=200)
    

saveEpisode = SaveEpisode.as_view()

class CreateEpisode(View):
    def post(self, request):
        data = json.loads(request.body)
        createEp(data)
        return HttpResponse(status=200)
    

createEpisode = CreateEpisode.as_view()