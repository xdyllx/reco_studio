from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse


def send_request(request):
    return HttpResponse("hello world")
