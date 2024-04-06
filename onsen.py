# -*- coding: UTF-8 -*-
import requests
import re
import codecs
import os
import sys
import io

#ffmpeg -i " + e + " -c copy " +name + '.ts'
#"ffmpeg -i " + name + '.ts' + " -write_xing 0 -id3v2_version 0 " + name + '.mp3' )
command = "ffmpeg -headers \"referer: https://www.onsen.ag/\""
w = open("fileWepUrl.txt", "a")

def programNames(url):
    urlSplit = url.split("/")
    program_name = urlSplit[len(urlSplit) - 1].strip()
    alternative_program_names = [program_name]
    if '_' in program_name:
        alternative_program_names.append(''.join(str.split(program_name, '_')))
    return alternative_program_names

def matchFileWebPath(reqText, programName):
    express = f'http((?!http).)*({programName})((?!http).)*m3u8'
    print(f'searching {express}')
    fileWepPath = re.search(express , reqText)
    return fileWepPath


def getMP3(url):
    try:
        program_names = programNames(url)
        print(program_names)

        req = requests.get(url)
        reqText = req.text
        # print(req)
        # print(b)
        
        for program_name in program_names:
            fileWepPath = matchFileWebPath(reqText, program_name)
            if fileWepPath:
                break
        if not fileWepPath:
            print("file not found")
            return
        
        fileWepPath = codecs.decode(fileWepPath.group(), 'unicode-escape')
        print(fileWepPath)

        fileName = re.search("((?!\/).)*(?:(\.mp))", fileWepPath)
        print(fileName)
        fileName = fileName.group().split('.')[0]

        commandInput =  "-i " + fileWepPath + " "
        commandOutput = " -acodec mp3 " + fileName + ".mp3"
        os.system(command +" -i " + fileWepPath + " -c copy "  +fileName + '.ts')
        os.system("ffmpeg -i " + fileName + '.ts' + " -write_xing 0 -id3v2_version 0 "  + fileName + '.mp3' )
        w.write(fileWepPath + "\n")
    except Exception as fileWepPath:
        print(fileWepPath)

f = open("urlLink.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
    getMP3(line)
f.close()
w.close()