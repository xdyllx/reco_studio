import base64

import random
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from storage import get_kcc_redis_resource

from follow.realtime_reco_pb2 import RealTimeRecoResponse

info_list0 = [{'name': 'InitProcessor', 'stage': 'pre', 'index': 0},
             {'name': 'PostProcessor', 'stage': 'post', 'index': 1}]
result_list0 = [[{'item_id': 1, 'item_type': 1}, {'item_id': 2, 'item_type': 1}],
               [{'item_id': 32, 'item_type': 1}, {'item_id': 33, 'item_type': 1}]]

def index(request):
    return render(request, 'index.html')


def send_request(request):
    key = str(random.randint(0, 9))
    redis_resource = get_kcc_redis_resource('kStepDebugInfoCache')
    encoded_req = redis_resource.get(key)

    url = 'http://td-dz-c463.yz:9080/realtime_reco'
    data = {'request': encoded_req}
    response = requests.post(url=url, data=data)
    response = response.json()
    decoded_response = base64.b64decode(response['response'])

    realtime_response = RealTimeRecoResponse()
    realtime_response.ParseFromString(decoded_response)

    info_list = list()
    result_list = list()

    for index, debug_log in enumerate(realtime_response.reco_debug_log):
        info_list.append({'name': debug_log.processor_class_name,
                          'stage': debug_log.stage_flag,
                          'index': index})
        length = len(debug_log.item_id)
        step_result_list = list()
        for i in range(length):
            step_result_list.append({'item_id': debug_log.item_id[i],
                                     'item_type': debug_log.item_type[i]})
        result_list.append(step_result_list)

    info_list_render = render_to_string('process.html', {'info_list': info_list})

    return JsonResponse({'status': 0, 'info_list_render': info_list_render, "result_list": result_list})

