import urllib.request
import urllib.parse
import re


def Url_Parser(url, values={}):
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    return respData
