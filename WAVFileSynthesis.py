from numpy import concatenate
import scipy.io.wavfile as wf
from pathlib import Path
def main():
    path=Path.cwd()
    waves=path.glob('*.wav')
    waves=list(waves)
    if len(waves)==0:
        print('当前目录下没有wav文件~')
        input('Press any key to exit...')
        return 0
    else:
        print('在当前目录下找到'+str(len(waves))+'个wav文件，开始合成')
    wavArry=[]
    formerR=0
    for wave in waves:
        currR,a=wf.read(str(wave))
        wavArry.append(a)
        print(str(wave))
    wavContent=concatenate(tuple(wavArry))
    wf.write(str(path/'合成音频.wav'),currR,wavContent)
    print(str(len(waves))+'个wav文件合成完成，合成的文件在当前目录下，被命名为：合成音频.wav')
    input('Press any key to exit...')
    
if __name__=='__main__':
    main()
