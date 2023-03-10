import psutil

print("CPU物理核心:",psutil.cpu_count(logical=False))
print("CPU逻辑数量:",psutil.cpu_count())
print("CPU使用占比:",psutil.cpu_percent(interval=1),"%")
mem = psutil.virtual_memory()
print("内存总量:",round(mem.total/1024/1024/1024,2),"GB")
print("内存使用量:",round(mem.used/1024/1024/1024,2),"GB")
print("内存空闲量:",round(mem.free/1024/1024/1024,2),"GB")
print("已使用内存占比:",mem.percent,"%")
disk_used = psutil.disk_usage('/')
print("磁盘总量:",round(disk_used.total/1024/1024/1024,2),"GB")
print("磁盘使用量:",round(disk_used.used/1024/1024/1024,2),"GB")
print("磁盘空闲量:",round(disk_used.free/1024/1024/1024,2),"GB")
print("已使用磁盘占比:",disk_used.percent,"%")