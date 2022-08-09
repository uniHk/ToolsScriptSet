# -*- coding: UTF-8 -*-
import os
import datetime

UnityPath = r"E:\Unity\Editor\Unity.exe"
ProjPath = r"E:\Project\\nssclient_publish\NssUnityProj"

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

    doCMD(UnityPath + " -batchmode -projectPath " + ProjPath)

main()
