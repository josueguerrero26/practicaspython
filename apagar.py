import os 

shutdown = input ("¿Quieres apagar el ordenador? (si/no): ")

if shutdown == 'si':
    os.system("shutdown /s /t 10")
else:
    exit()