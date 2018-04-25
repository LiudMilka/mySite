from django.http import HttpResponse
import datetime
import requests
from dateutil.parser import parse


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def image(request):
    html = "<html><body><img src=\"http://theoldreader.com/kittens/500/500\"/></body><html>"
    return HttpResponse(html)

def weather(request):
    url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22kyiv%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    data = requests.get(url).json()
    forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
    forecast = []
    for day_data in forecast_data:
        forecast.append({
            "data": parse(day_data["data"]),
            "high_temp": day_data["high"]
        })
    return forecast
