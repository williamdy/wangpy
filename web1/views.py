# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
import json
import openstack
from pyVim import connect
import atexit


# 将请求定位到index.html文件中
def index(request):
    return render(request, 'index.html')


def test_get(request):
    if request.method == "GET":
        param = json.dumps(request.GET)
        return HttpResponse("this is get response " + param)
    elif request.method == "POST":
        return HttpResponse("this is  POST response")


def openstack_test(request):
    # Initialize and turn on debug logging
    openstack.enable_logging(debug=True)

    # Initialize cloud
    conn = openstack.connect(cloud='test_cloud')
    result = "";
    for server in conn.compute.servers():
        print(server.to_dict())
        result = json.dumps(server.to_dict())
    return HttpResponse(result);


def vsphere_test(request):
    service_instance = connect.SmartConnectNoSSL(host='10.0.38.74',
                                                 user='administrator@vsphere.local',
                                                 pwd='Sugon;123',
                                                 port=int(443))
    atexit.register(connect.Disconnect, service_instance)
    session_id = service_instance.content.sessionManager.currentSession.key
    result = session_id
    return HttpResponse(result);
