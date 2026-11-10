import psutil
from platform import python_version,platform,machine
from distro import os_release_info
from subprocess import run

run(["ncdu","-o","home_dir_stats.txt",""],shell = False,text = True, capture_output = False)
run(["ncdu","-o","root_dir.txt","/"],shell = False,text = True, capture_output = False)

run(["sed","-i","1d","root_dir.txt"],shell = False,text = True, capture_output = False)
run(["sed","-i","1d","home_dir_stats.txt"],shell = False, text = True, capture_output = False)


def convert_to_GB(mem_value):

    convert = lambda int_value:round(int_value/1e+6,2)
    return convert(mem_value)

#----sys_info----

distro_info = os_release_info()["pretty_name"] #Name of linux distro and version id
hardware_arch = machine() # Hardware Architecture
python_version = python_version() # Python Version
kernel_desc = platform() # Provides Kernel Description
hostname  = run(["uname","-n"],shell = False, text = True,capture_output = True).stdout.strip() # Network Hostname
uptime = run(["uptime","-p"],shell = False, text = True, capture_output = True).stdout.strip()  # Uptime 
shell = run(["neofetch","--stdout","|","grep","-wi","shell"],shell = False,text = True, capture_output = True).stdout.strip() # Shell Type and Version
avg_sys_load = list(map(lambda num:round(num,2),psutil.getloadavg())) # Average System Load rounded to 2 d.p



if psutil.sensors_battery() is not None:

    bat_stats = [round(psutil.sensors_battery()[0]),psutil.sensors_battery()[-1],psutil.sensors_battery()[1]]
    
    #round(psutil.sensors_battery()[0]) - Returns and rounds current percent 
    #psutil.sensors_battery()[-1] - Returns boolean value True if machine is charging. Otherwise false. 
    #psutil.sensors_battery()[1] - Returns the estimated battery life remaining

cpu_labels = ("model name","cache size","cpu cores")
mem_labels = ("MemAvailable:","MemFree:","MemTotal:")

cpu_info_file = open("/proc/cpuinfo","r").readlines()
mem_info_file = open("/proc/meminfo","r").readlines()
cpu_info_file.extend(mem_info_file)

cpu_specs,mem_specs = [],[]

for comp_info in cpu_info_file:


    if comp_info.strip().startswith(cpu_labels) == True and len(cpu_specs)<3:
        cpu_specs.append(comp_info.strip()[comp_info.index(":")+1:].strip())

    elif comp_info.strip().startswith(mem_labels) == True and len(mem_specs)<3:
        mem_specs.append(int(comp_info.strip()[comp_info.index(":")+1:comp_info.index("k")].strip()))


proc_info = []    

for proc in psutil.process_iter(): 

    proc_info.append([proc.pid,proc.name(),proc.status()])
