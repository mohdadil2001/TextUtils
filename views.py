## i have created this file - adil
from django.http import HttpResponse
from django.shortcuts import render

def ex1(request):
    s='''<h2>Navigation Bar</h2>
    <a href='https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12' >Django with harry bhaii</a>
    <a href='https://www.youtube.com'>You Tube</a><br>
    <a href='https://www.facebook.com'>facebook</a><br>
    <a href='https://www.google.com'>google</a><br>
    <a href='https://www.flipkart.com'>flipkart</a><br>'''
    return HttpResponse(s)

def index(request):
    # analys the text 
    return render(request,'index.html' )
    # return HttpResponse("Home")

def analyze(request):
    # get the text
    djtext=request.POST.get('text','default')
    # cheack box values 
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    

    # analyzed=djtext
    
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed +char
                
        params={'purpose':'Remove Punctuation' ,'Analyzed_text':analyzed }
    # Analyze the text
    djtext=analyzed
        # return render(request,'analyze.html',params)

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()

            params={'purpose':'Change to uppercase' ,'Analyzed_text':analyzed }
    # Analyze the text
    djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char 

            params={'purpose':'Removes New Lines' ,'Analyzed_text':analyzed }
    # Analyze the text
    djtext=analyzed
        # return render(request,'analyze.html',params)

    if extraspaceremover=="on":
        extrspc=""
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1]==" ":
                pass
            else:
                extrspc=extrspc+char 

            params={'purpose':'Removes New Lines' ,'Analyzed_text':extrspc }
    # Analyze the text
    djtext=analyzed
        # return render(request,'analyze.html',params)
    
    if charcount=="on":
        analyzed=0
        for char in djtext:
            if char==" ":
                pass
            else:
                analyzed=analyzed+1 

        params={'purpose':'Removes New Lines' ,'Analyzed_text':analyzed }
    # Analyze the text

    if charcount!="on" and extraspaceremover!="on" and newlineremover!="on" and fullcaps!="on" and removepunc!='on':
        return HttpResponse("pleas kuch to on karo !!! ")
    return render(request,'analyze.html',params)