from django.shortcuts import render
from django.http import HttpResponse
from . import tasks


def handle_user_data_sync(request):
    task = tasks.send_sms_to_user.apply_async()
    task.get()
    return HttpResponse("<h1> sync view </h1>")


def handle_user_data_async(request):
    task = tasks.send_sms_to_user.apply_async()
    return HttpResponse("<h1> async view </h1>")
