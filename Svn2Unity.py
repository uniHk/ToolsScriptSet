# -*- coding: UTF-8 -*-
import os
import datetime

UnityPath = r"J:\Unity\Editor\Unity.exe"

def doCMD(cmd):
    print(cmd)
    os.system(cmd)

def main():
    ProjPath = os.getcwd() + r"\NssUnityProj"
    print(ProjPath)

    count = 0
    while count < 10:
        doCMD("svn cleanup")
        doCMD("svn up --accept=tf")
        count += 1

    unityImportStartTime = datetime.datetime.now()
    print("\n\n\nunityImportStartTime = %s\n\n\n" % (unityImportStartTime))

    doCMD(UnityPath + " -batchmode -projectPath " + ProjPath)

main()
