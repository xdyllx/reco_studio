from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
import requests
import base64
from follow.realtime_reco_pb2 import RealTimeRecoRequest, RealTimeRecoResponse
from google.protobuf.json_format import MessageToDict

def send_request(request):
    url = 'http://td-dz-c463.yz:9080/realtime_reco'
    data = {}
    response = requests.post(url=url, data=data)
    response = response.json()
    decoded_response = base64.b64decode(data['response'])

    realtime_response = RealTimeRecoResponse()
    realtime_response.ParseFromString(decoded_response)

    result = MessageToDict(realtime_response, preserving_proto_field_name=True, use_integers_for_enums=True)
    return HttpResponse("hello world")
