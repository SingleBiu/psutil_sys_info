import psutil as ps
import socket
import uuid
import datetime

# 获取MAC地址


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])


def get_computer_info():
    # 获取主机名
    hostname = socket.gethostname()
    # 获取IP
    ip = socket.gethostbyname(hostname)
    # 系统用户
    users_list = ",".join([u.name for u in ps.users()])
    # 系统启动时间
    start_time = datetime.datetime.fromtimestamp(
        ps.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    sys_info = {"Hostname": hostname,
                "IP": ip,
                "MAC": get_mac_address(),
                "User": users_list,
                "Start time": start_time}

    # 1 CPU信息
    # CPU物理核心
    cpu_count = ps.cpu_count(logical=False)
    # CPU逻辑数量
    cpu_logical = ps.cpu_count()

    cpu_info = {"CPU amount：": cpu_count,
                "CPU logical": cpu_logical}

    # 2 内存信息
    mem = ps.virtual_memory()
    # 内存总量
    mem_total = round(mem.total/1024/1024/1024, 2)
    # 内存使用量
    mem_used = round(mem.used/1024/1024/1024, 2)
    # 内存空余量
    mem_free = round(mem.free/1024/1024/1024, 2)
    # 内存使用百分比
    mem_percent = mem.percent

    mem_info = {"Total memory:": str(mem_total)+"GB",
                "Memory used:": str(mem_used)+"GB",
                "Memory free:": str(mem_free)+"GB",
                "Memory usage:": str(mem.percent)+"%"}

    # 3 磁盘信息
    io = ps.disk_partitions()
    disk_info = []
    for i in io:
        disk = ps.disk_usage(i.device)
        disk_data = {"disk_name": i.device,
                     "total": str(round(disk.total / 1024/1024/1024, 1))+"GB",
                     "used": str(round(disk.used/1024/1024/1024, 1))+"GB",
                     "surplus": str(round(disk.free/1024/1024/1024, 1))+"GB",
                     "rate": str(ps.disk_usage(i.device).percent)+"%"}
        disk_info.append(disk_data)

    # 4 网卡信息
    net = ps.net_io_counters()
    bytes_sent = '{0:.2f}'.format(net.bytes_recv / 1024 / 1024)
    bytes_rcvd = '{0:.2f}'.format(net.bytes_sent / 1024 / 1024)
    net_info = {"bytes_sent": bytes_sent+"MB",
                "bytes_rcvd": bytes_rcvd+"MB"}

    # 数据字典
    data = {"sys_info": sys_info, "cpu_info": cpu_info,
            "mem_info": mem_info, "disk_info": disk_info, "net_info": net_info}
    return data

data = get_computer_info()
print(data)