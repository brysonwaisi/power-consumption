from django.shortcuts import render
import time
import psutil


def get_cpu_usage_for_app(app_name):
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        if proc.info['name'] == app_name:
            return proc.info['cpu_percent']
    return 0.0

def display_usage(cpu_usage, mem_usage, bars=25):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = chr(124) * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = chr(124) * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    return f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  MEM Usage: |{mem_bar}| {mem_usage:.2f}%  "

def monitor_cpu(request):
    running_processes = [proc.info['name'] for proc in psutil.process_iter(['name'])]

    if request.method == 'POST':
        app_name = request.POST.get('app_name', None)
        if app_name in running_processes:
            target_app_cpu_usage = get_cpu_usage_for_app(app_name)
            usage_text = display_usage(target_app_cpu_usage, psutil.virtual_memory().percent, 30)
        else:
            target_app_cpu_usage = None
            usage_text = "Invalid application name. Please enter a valid application name."
    else:
        app_name = None
        target_app_cpu_usage = None
        usage_text = ""

    return render(request, 'cpu_monitor/monitor_cpu.html', {
        'running_processes': running_processes,
        'app_name': app_name,
        'target_app_cpu_usage': target_app_cpu_usage,
        'usage_text': usage_text,
    })

