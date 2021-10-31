import wmi
import time
import os
import datetime

os.system('mode con: cols=30 lines=10')
os.system("title XerosLab - HWLogger")

now = datetime.datetime.now()
currentDirPath = os.path.dirname(os.path.realpath("__file__"))

os.startfile(os.path.join(currentDirPath, "Core.exe"))

logFileName = now.strftime("%Y-%m-%d %H-%M-%S.log")

w = wmi.WMI(namespace="root\OpenHardwareMonitor")

while True:
    f = open(os.path.join(currentDirPath, "logs", logFileName),
             mode='a', encoding='utf8')
    result = []
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType == 'Temperature':
            temperature = (sensor.Name, sensor.Value)
            if temperature[0].startswith("CPU"):
                result.append(temperature)
            elif temperature[0].startswith("GPU"):
                result.append(temperature)
    os.system("cls")
    try:
        print("{} : {}°C".format(result[0][0], result[0][1]))
        print("{} : {}°C".format(result[1][0], result[1][1]))
        print("{} : {}°C".format(result[2][0], result[2][1]))

        now = datetime.datetime.now()
        f.write(now.strftime("[ %H:%M:%S ]\n"))
        f.write("{} : {}°C\n".format(result[0][0], result[0][1]))
        f.write("{} : {}°C\n".format(result[1][0], result[1][1]))
        f.write("{} : {}°C\n\n".format(result[2][0], result[2][1]))
        time.sleep(1)
    except:
        print("Core.exe를 실행해주세요")
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
