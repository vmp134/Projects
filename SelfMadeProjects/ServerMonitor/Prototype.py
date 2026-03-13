import time
import psutil

def displayUsage(cpuUsage, memUsage, bars=50):
    cpu = cpuUsage/100.0
    cpu_bar = '[' + ('█' * int(cpu * bars)) + ('-' * (bars- int(cpu * bars))) + ']'

    mem = memUsage/100.0
    mem_bar = '['+ ('█' * int(mem * bars)) + ('-' * (bars- int(mem * bars))) + ']'

    print(f"\rCPU: {cpu_bar} {cpuUsage:.2f}%  ", end="")
    print(f"MEM: {mem_bar} {memUsage:.2f}%  ", end="\r")

while True:
    displayUsage(psutil.cpu_percent(), psutil.virtual_memory().percent, 20)
    time.sleep(0.5)
