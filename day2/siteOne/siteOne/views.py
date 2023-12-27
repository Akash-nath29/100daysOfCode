#Self made file
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<a href='https://stackoverflow.com'>StackOverFlow</a><br><a href='https://github.com'>Github</a><br><a href='https://www.google.com'>Google</a>")

# def about(request):
#     return HttpResponse("Hii")

def index(request):
    # return HttpResponse("Home<br><a href='/removepunc'>Remove Punc</a>")
    return render(request, 'index.html')

def analyze(request):
    text = request.GET.get('text', 'default')
    remove = request.GET.get('analyze', 'off')
    params = {
        'purpose': 'Remove Punctuation',
        'analyzed_text': text
    }
    return render(request, 'analyze.html', params)

# def makecap(request):
#     return HttpResponse("Make caps Page")

# def newlineRemove(request):
#     return HttpResponse("NewLine Remove Page.")

# def spaceRemove(request):
#     return HttpResponse("space Remove Page.")

# def charCount(request):
#     return HttpResponse("Character Count Page.")