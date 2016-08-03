#codeing utf-8

import os, sys 

def convert(filename):
    vtt = open(filename)
    vtt_data = vtt.read()
    vtt_data = vtt_data.replace('.', ',')
    vtt_data = vtt_data[7:]
    srt = open(filename.replace("vtt", "srt"), 'w')
    srt.write(vtt_data)
    vtt.close()
    srt.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        path = "./"
    else:
        path = sys.argv[1]

    if os.path.isdir(path):
        for i in os.listdir(path):
            filename, file_ext = os.path.splitext(i)
            if file_ext == ".vtt":
                print("convert %s ..." % i)
                convert(os.path.join(path, i))
    else:
        print("Usage: vtt2srt [path]")
        
