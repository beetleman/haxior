# -*- coding: utf-8 -*-

# from django.shortcuts import render
from django.http import HttpResponse
import httplib2
from urllib import urlencode
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import re

from models import Dane

PROXY_FORMAT = u"http://%s/%s" % (settings.PROXY_DOMAIN, u"%s")
RE_HAX = re.compile(
    '(%s.+index.php)|(%s.+view.php)' % (
        settings.PROXY_DOMAIN,
        settings.PROXY_DOMAIN
    ),
    re.VERBOSE
)


def replacer(match):
    text = match.group()
    # import ipdb; ipdb.set_trace()
    return text.replace(
        settings.PROXY_DOMAIN,
        settings.HAXIOR_DOMAIN
    )


@csrf_exempt
def proxy(request, url):
    conn = httplib2.Http()
    m = Dane()
    if request.method == "GET":
        url_ending = "%s?%s" % (url, urlencode(request.GET))
        url = PROXY_FORMAT % url_ending
        resp, content = conn.request(url, request.method)
        m.type = m.GET
        data_to_save = dict(request.GET.iterlists())
    elif request.method == "POST":
        url = PROXY_FORMAT % url
        data = urlencode(request.POST)
        resp, content = conn.request(url, request.method, data)
        m.type = m.POST
        data_to_save = dict(request.POST.iterlists())
    if data_to_save:
        m = Dane()
        m.data = str(data_to_save)
        m.url = url
        m.save()
    return HttpResponse(RE_HAX.sub(
        replacer,
        content
    ))
