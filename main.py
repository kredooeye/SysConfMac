# Скрипт для сбора данных о конфигурации системы на MacOS с использованием OS с сохранением в формате Json

import os
import json

system = os.uname()
disk = os.statvfs('/')

page_size = os.sysconf('SC_PAGE_SIZE')
page_count = os.sysconf('SC_PHYS_PAGES')

total_memory = page_size * page_count
total_disk_space = disk.f_frsize * disk.f_blocks
free_disk_space = disk.f_frsize * disk.f_bavail

configuration = {
    "system": {
        "name": system.sysname,
        "hostname": system.nodename,
        "kernel_release": system.release,
        "kernel_version": system.version,
        "architecture": system.machine
    },
    "processor": {
        "logical_cores": os.cpu_count(),
    },
    "memory": {
        "total_bytes": total_memory,
        "total gb": round(total_memory / (1024 ** 3), 2)
    },
    "disk": {
        "total_bytes": total_disk_space,
        "free_bytes": free_disk_space,
        "total gb": round(total_disk_space / (1024 ** 3), 2),
        "free gb": round(free_disk_space / (1024 ** 3), 2)
    },
    "network": {
        "interfaces": os.listdir('/sys/class/net/')
    }
}

with open('system_configuration.json', 'w', encoding='utf-8') as json_file:
    json.dump(configuration, json_file, ensure_ascii=False, indent=4)

print("System configuration data has been saved to 'system_configuration.json'.")
