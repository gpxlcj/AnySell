#! -*- coding:utf8 -*-
__author__ = 'gpxlcj'
from django.shortcuts import render_to_response, render
from django.http import HttpResponse
import json

def render_json(data):

    temp_json = json.dumps(data, ensure_ascii=False)
    httpresponse = HttpResponse(temp_json, mimetype="application/json")
    return httpresponse