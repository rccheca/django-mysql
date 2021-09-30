from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


def myview(request):
    count = request.session.get('count', 0) + 1
    request.session["count"] = count
    resp = HttpResponse(f"Hello, world. {request.session['dj4e']} Hello app, view count={count}")
    resp.set_cookie('dj4e_cookie', 'f331c4fb', max_age=1000)
    return resp
