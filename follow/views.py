import base64

import random
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from storage import get_kcc_redis_resource

from follow.realtime_reco_pb2 import RealTimeRecoRequest, RealTimeRecoResponse

info_list0 = [{'name': 'InitProcessor', 'stage': 'pre', 'index': 0},
             {'name': 'PostProcessor', 'stage': 'post', 'index': 1}]
result_list0 = [[{'item_id': 1, 'item_type': 1}, {'item_id': 2, 'item_type': 1}],
               [{'item_id': 32, 'item_type': 1}, {'item_id': 33, 'item_type': 1}]]

def index(request):
    return render(request, 'index.html')


def send_request(request):
    key = str(random.randint(0, 9))
    redis_resource = get_kcc_redis_resource('xStepDebugInfoCache')
    serialized_req = redis_resource.get(key)
    encoded_req = base64.b64encode(serialized_req)
    req = RealTimeRecoRequest()
    req.ParseFromString(serialized_req)
    user_info = dict()
    user_info['user_id'] = req.user_id
    # user_info['device_id'] = req.device_id

    url = 'http://td-dz-c463.yz:29080/realtime_reco'
    data = {'request': encoded_req}
    response = requests.post(url=url, data=data)
    response = response.json()
    print(response['code'])
    print(response.get('reason'))
    decoded_response = base64.b64decode(response['response'])

    realtime_response = RealTimeRecoResponse()
    realtime_response.ParseFromString(decoded_response)

    info_list = list()
    result_list = list()
    print("debug log size", len(realtime_response.reco_debug_log))
    print("debug log 0", realtime_response.reco_debug_log[0])
    for index, debug_log in enumerate(realtime_response.reco_debug_log):
        length = len(debug_log.item_id)
        info_list.append({'name': debug_log.processor_class_name,
                          'stage': debug_log.stage_flag,
                          'index': index,
                          'num': length})
        step_result_list = list()
        for i in range(length):
            step_result_list.append({'item_id': debug_log.item_id[i],
                                     'item_type': debug_log.item_type[i],
                                     'reason': debug_log.source_type[i]})
        result_list.append(step_result_list)
    info_list.append({'name': "final response",
                      'stage': 'final',
                      'index': len(realtime_response.reco_debug_log),
                      'num': len(realtime_response.follow_result)})
    final_result = list()
    for item in realtime_response.follow_result:
        final_result.append({
            'item_id': item.id,
            'type': item.type,
            'reason': item.reason,
        })
    result_list.append(final_result)


    info_list_render = render_to_string('process.html', {'info_list': info_list})
    print("info_list", info_list)
    return JsonResponse({'status': 0, 'user_info': user_info, 'info_list_render': info_list_render, "result_list": result_list})

