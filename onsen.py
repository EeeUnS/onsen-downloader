# -*- coding: UTF-8 -*-
import requests
import re
import codecs
import os
import sys
import io

# ffmpeg -i " + e + " -c copy " +name + '.ts'
# "ffmpeg -i " + name + '.ts' + " -write_xing 0 -id3v2_version 0 " + name + '.mp3' )
command = "ffmpeg -headers \"referer: https://www.onsen.ag/\""
w = open("fileWepUrl.txt", "a")


def GetProgramNames(sUrl):
    dicUrlSplit = sUrl.split("/")
    sProgramName = dicUrlSplit[len(dicUrlSplit) - 1].strip()
    dicProgramNames = [sProgramName]
    if '_' in sProgramName:
        dicProgramNames.append(''.join(str.split(sProgramName, '_')))
    return dicProgramNames


def GetFileWebPath(sReqText, sProgramName):
    express = f'http((?!http).)*({sProgramName})((?!http).)*m3u8'
    print(f'searching {express}')
    sFileWepPath = re.search(express, sReqText)
    return sFileWepPath


def getMP3(url):
    try:
        sProgramNames = GetProgramNames(url)
        print(sProgramNames)

        req = requests.get(url)
        reqText = req.text
        # print(req)
        # print(b)

        for sProgramName in sProgramNames:
            sFileWepPath = GetFileWebPath(reqText, sProgramName)
            if sFileWepPath:
                break
        if not sFileWepPath:
            print("sFileWepPath not found", sProgramNames)
            raise Exception("sFileWepPath not found")


        sFileWepPath = codecs.decode(sFileWepPath.group(), 'unicode-escape')
        print(sFileWepPath)

        fileName = re.search("((?!\/).)*(?:(\.mp))", sFileWepPath)
        print(fileName)
        fileName = fileName.group().split('.')[0]

        commandInput = "-i " + sFileWepPath + " "
        commandOutput = " -acodec mp3 " + fileName + ".mp3"
        os.system(command + " -i " + sFileWepPath + " -c copy " + fileName + '.ts')
        os.system("ffmpeg -i " + fileName + '.ts' + " -write_xing 0 -id3v2_version 0 " + fileName + '.mp3')
        w.write(sFileWepPath + "\n")
    except Exception as sFileWepPath:
        print(sFileWepPath)


f = open("urlLink.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
    getMP3(line)
f.close()
w.close()