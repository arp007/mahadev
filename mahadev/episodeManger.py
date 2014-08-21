from models import Episode, Series, SeriesSequence
import time
from datetime import datetime

def sav(data):
    ep = Episode.objects.all()[0]
    series = Series()
    series.link = data.get("serieslink")
    series.date = convStrToDate(data.get('date'))
    series.thumbnail_url = data.get('thumbnail')
    series.episode = ep
    series.save()
    return series
    
def savSeq(data, series):
    seriesSequence = data.get('seriesSequence')
    for s in seriesSequence:
        sSeq = SeriesSequence()
        sSeq.link = s.get('link')
        sSeq.iframe_link = s.get('iframe_link')
        sSeq.source = s.get('source')
        sSeq.thumbnail_url = s.get('thumbnail_url')
        sSeq.seq_num = s.get('seq_num')
        sSeq.series = series
        sSeq.save()

def createEp(data):
    ep = Episode()
    ep.name = data.get('name')
    ep.date = convStrToDate(data.get('date'))
    ep.link = data.get('link')
    ep.thumbnail_url = data.get('thumbnail_url')
    ep.save()


def convStrToDate(str_date):
    
    time_string = removePosStr(str_date)
    print time_string
    strp_time = time.strptime(time_string, '%d %B %Y')
    date_django = datetime.fromtimestamp(time.mktime(strp_time))
    return date_django



def removePosStr(date):
    dt = date.split(" ")
    dig = dt[0].replace("th","")
    dig = dig.replace("st","")
    dig = dig.replace("rd","")
    str_date = "{} {} {}".format(dig,dt[1], '2014')
    return str_date
   

