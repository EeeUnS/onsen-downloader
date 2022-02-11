# onsen-downloader

this is managed repo

音泉(onsen) radio downloader.
Download latest episode.

download [release](https://github.com/EeeUnS/onsen-downloader/releases) `onsen-downloader.zip`

1. unpack onsen-downloader.zip in folder
  - ffmpeg.exe
  - onsen.exe
  - urlLink.txt
  - README.md
  (`onsen.exe` inside using`ffmpeg.exe`)
2. redio url add to `urlLink.txt`. see example in `urlLink.txt`
3. onsen.exe so make ts & mp3

After using onsen.exe, urlLink.txt is created. Here, the file url used to download the file is stored, and you can directly re-download it by entering the command from cmd.

If there is a problem with the occurrence of an error, etc., try running it in the cmd window (the window does not turn off and the log remains) and put the error as an issue.

Follow commands sequentially.

ffmpeg -headers \"referer: https://www.onsen.ag/\" -i   fileurl  -c copy  createFileName1.ts
ffmpeg -i createFileName1.ts -write_xing 0 -id3v2_version 0  createFileName2.mp3

------------------------

onsen 최신회차 라디오를 다운로드합니다.

사용법
1. [release](https://github.com/EeeUnS/onsen-downloader/releases)에서  onsen-downloader.zip를 다운받습니다.  압축을풀면 다음이 한폴더에 존재합니다
  - ffmpeg.exe
  - onsen.exe
  - urlLink.txt
  - README.md
  `onsen.exe`가 내부적으로 `ffmpeg.exe`를 사용합니다.)

2. 듣는 onsen url를 텍스트파일 안에 넣습니다. txt 파일안에 있는 url을 보면 대충 넣어야하는 url이 어떤건지, 어떻게 넣어야하는지 감이 잡힙니다.
3. `onsen.exe` 실행하면 ts파일과 mp3파일이 생성됩니다. 

onsen.exe 사용후에는 urlLink.txt 이 생성 되어있습니다. 여기에는 파일을 다운로드 받는데 사용하는 파일 url 이 저장되어있으며 cmd에서 커맨드를 입력해 직접 다시 다운받을 수 있습니다.

아래 커맨드를 순차적으로 실행


ffmpeg -headers \"referer: https://www.onsen.ag/\" -i   파일url  -c copy  생성파일명1.ts
ffmpeg -i 생성파일명1.ts -write_xing 0 -id3v2_version 0  생성파일명2.mp3

혹시 에러 발생등으로 문제가 있을시에는 cmd 창에서 실행을 해보고(창이 안꺼지고 로그가 남아있음) 에러를 이슈로 넣어주세요.


Thanks to ㅋㅋ(210.197)




