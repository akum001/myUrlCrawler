from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import condition
from .forms import SearchForm
from .utils import stream_response


def index(request):
    return render(request, 'mycrawler/index.html')


@condition(etag_func=None)
def search(request):
    if request.method == 'POST':
        print(request.POST['url'])
        print(request.POST)
        form = SearchForm(request.POST)
        if form.is_valid():
            link_list  = stream_response(request.POST['url'], request.POST['depth'])
            return render(request, 'mycrawler/search.html', {'links' : link_list})
