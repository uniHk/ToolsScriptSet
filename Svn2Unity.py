# -*- coding: UTF-8 -*-
import os
import datetime

def doCMD(cmd):
    print(cmd)
    os.system(cmd)

def main():
    count = 0
    while count < 10:
        doCMD("svn cleanup")
        doCMD("svn up --accept=tf")
        count += 1

    unityImportStartTime = datetime.datetime.now()
    print("\n\n\nunityImportStartTime = %s\n\n\n" % (unityImportStartTime))

    doCMD(r"E:\Unity\Editor\Unity.exe -batchmode -projectPath E:\Project\Trunk_backup\NssUnityProj")

main()
