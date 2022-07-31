from django.shortcuts import render, redirect
from django.urls import reverse
from  .forms  import  URLForm   
from  .models  import URLShorten   
from django.views import View


class URLShortenView(View):
    def get(self, request):
        form = URLForm()
        return render(request, 'shortner/index.html', context={'form': form})
    
    def post(self, request):
        form = URLForm(request.POST)

        if form.is_valid():
            form.save()
            url = form.cleaned_data['url']
            pk = URLShorten.objects.filter(url=url)[0].short

            # print('\n', pk, url, sep = ' - ', end='\n\n')
            return render(request, 'shortner/thanks.html', context={'id': pk})
        return render(request, 'shortner/index.html', context={'form': form})


def short_url(request, code):
    url = URLShorten.objects.filter(short= code)[0].url
    return redirect(url)