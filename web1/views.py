# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
import json
import openstack
from pyVim import connect
import atexit
from web1.api.models import VM
from web1.api.serializers import VMSerializer


# 将请求定位到index.html文件中
def index(request):
    return render(request, 'index.html')


def test_get(request):
    if request.method == "GET":
        param = json.dumps(request.GET)
        return HttpResponse("this is get response " + param)
    elif request.method == "POST":
        return HttpResponse("this is  POST response")


def openstack_vm_action(request):
    # Initialize and turn on debug logging
    openstack.enable_logging(debug=True)
    id = ""
    if request.method == "GET":
        param = json.dumps(request.GET)
        id = request.GET.get('id')
        action = request.GET.get('action')

    elif request.method == "POST":
        id = request.POST.get('id')
        action = request.POST.get('action')

    # Initialize cloud
    conn = openstack.connect(cloud='test_cloud')
    result = ""
    server = conn.compute.find_server(id)
    if action == "reboot":
        conn.compute.reboot_server(id, reboot_type="soft")

    if action == "power_off":
        conn.compute.stop_server(id)

    if action == "power_on":
        conn.compute.start_server(id)

    if action == "shelve":
        conn.compute.shelve_server(id)

    if action == "unshelve":
        conn.compute.unshelve_server(id)

    if action == "pause":
        conn.compute.pause_server(id)

    if action == "unpause":
        conn.compute.unpause_server(id)

    if action == "terminate":
        conn.compute.delete_server(id)

    result = json.dumps(server.to_dict())
    return HttpResponse(result)


def openstack_test(request):
    # Initialize and turn on debug logging
    openstack.enable_logging(debug=True)

    # Initialize cloud
    conn = openstack.connect(cloud='test_cloud')
    result = ""
    for server in conn.compute.servers():
        status = server.vm_state
        name = server.name
        id = server.id
        vm = VM(id, name, status)
        vm.save()
        value = id + "," + name + "," + status + "\n\r\t"
        print(value)
        result += value
    return HttpResponse(result)


def vsphere_test(request):
    service_instance = connect.SmartConnectNoSSL(host='10.0.38.74',
                                                 user='administrator@vsphere.local',
                                                 pwd='Sugon;123',
                                                 port=int(443))
    atexit.register(connect.Disconnect, service_instance)
    session_id = service_instance.content.sessionManager.currentSession.key
    result = session_id
    return HttpResponse(result)
