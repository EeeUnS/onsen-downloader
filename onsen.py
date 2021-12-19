import requests
import re
import codecs
import os

command = 'youtube-dl.exe  --add-header Accept:"*/*" --add-header Accept-Encoding:"gzip, deflate, br" --add-header Accept-Language:"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6" --add-header Connection:"keep-alive" --add-header Host:"onsen-ma3phlsvod.sslcs.cdngc.net" --add-header Origin:"https://www.onsen.ag" --add-header Referer:"https://www.onsen.ag/" --add-header "sec-ch-ua: Google Chrome;v=95, Chromium;v=95, ;Not A Brand;v=99" --add-header sec-ch-ua-mobile:"?0" --add-header sec-ch-ua-platform:""Windows"" --add-header Sec-Fetch-Dest:"empty" --add-header Sec-Fetch-Mode:"cors" --add-header Sec-Fetch-Site:"cross-site" --add-header User-Agent:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"  --extract-audio  --audio-format mp3 '

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
        output_file = "-o \"" + name +  ".mp3\"  "
        print(output_file)
        print(name)
        
        print(command + output_file + e)
        os.system(command + output_file + e)
    except Exception as e:
        print(e)

f = open("urlLink.txt", 'r')
for line in f:
    getMP3(line)
