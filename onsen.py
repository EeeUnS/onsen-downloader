import requests
import re
import codecs
import os

#https://onsen-ma3phlsvod.sslcs.cdngc.net/onsen-ma3pvod/_definst_/202102/iine2102258sid-36.mp4/playlist.m3u8
# url = 'https://www.onsen.ag/program/iine'
# url2 = 'https://www.onsen.ag/program/kokuradio'


def getMP3(url):
    try:
        req =requests.get(url)
        b = req.text
        a = re.search("http((?!http).)*m3u8", b)
        if not a :
            print("error")

        e = codecs.decode(a.group(), 'unicode-escape')
        print(e)
        name = re.search("((?!\/).)*(?:(\.mp))", e)
        name = name.group().split('.')[0]

        print(name)

        os.system(f"ffmpeg -i {e} -c copy {name}.ts")
        os.system(f"ffmpeg -i {name}.ts -write_xing 0 -id3v2_version 0 {name}.mp3")

    except Exception as e:
        print(e)


f = open("urlLink.txt", 'r')
for line in f:
    getMP3(line)


