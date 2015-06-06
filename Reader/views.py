from django.shortcuts import render_to_response,render
from django.template import RequestContext
# Create your views here.
from urllib import urlopen
import feedparser


def parse(request):
    
    
    if request.POST:
        webpage =  urlopen(request.POST['term']).read()
        feed_dict = feedparser.parse(webpage)
        print feed_dict
        return render(request, 'result2.html', {'results': feed_dict})
    else:
        return render_to_response('result.html',context_instance=RequestContext(request))
    