''''''

import threading
import time

def download_file(file):
    print("downloading",file)
    time.sleep(2)
    print(file,"finished")
files = ["movie.mp4","song.mp3","image.jpg"]
threads = []
for f in files:

 t = threading.Thread(target=download_file,args=(f,))
threads.append(t)
t.start()
for t in threads:
    t.join()
print("all downloads in finished")












