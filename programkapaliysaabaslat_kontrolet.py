import os
import time
import shutil  #pip install psutil==5.9.2
import psutil





def findProcessIdByName(processName):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects;

def exesorgu():
    listOfProcessIds = findProcessIdByName('osk')
    if len(listOfProcessIds) > 0:
        for elem in listOfProcessIds:
            processID = elem['pid']
            processName = elem['name']
            processCreationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))


    else:
        print(' Ekran klavyesi bulunamadı. Başlatılıyor....')   #komut satırında gözükür
        os.system('osk')




while True:
    exesorgu()
    time.sleep(5)