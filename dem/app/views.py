from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse


def test(request):
    return HttpResponse('hghgkj')

def top(request):
    return HttpResponse('TOP')

def last(request):
    return HttpResponse('last')

def user(request):
    login = request.GET.get('login')
    password = request.GET.get('password')
    return HttpResponse(f'login: {login} <br> password: {password}')

def about(request):
    return HttpResponsePermanentRedirect('/')

def contacts(request):
    return HttpResponseRedirect('/')
    

def error(request):
    return HttpResponseNotFound('404')

def acces(request):
    login = request.GET.get('login')
    password = request.GET.get('password')
    if login == 'admin' and password == 'admin':
       return HttpResponse('все норм')
    else: 
        return HttpResponse('доступ закрыт')

def likes(request, id = 0):
    like = request.GET.get('likes')
    comment = request.GET.get('comments')
    return HttpResponse(f'likes {like} <br> comments {comment}')

def response(request):
    return JsonResponse({"name": "dan", "surname": "dem"})


def cookies(request):
    login = request.GET.get('login')
    response= HttpResponse(login)
    response.set_cookie('login', login)
    return response

def get(request):
    login = request.COOKIES['login']
    return HttpResponse(f'Hello {login}')