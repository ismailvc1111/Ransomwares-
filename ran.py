import os
import socket
home = os.environ['HOME']
carpetas =  os.listdir(home)
carpetas = [x for x in carpetas  if not x.strartswitch('.')]
extension = ['.mp4','.mp3','.avi']

def check_internet():
   s = socket.socket(soocket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(2)
    try:
        s.connect(('socket.io',80))
        s.close()
    except:
        exit()

def discover():
      file_list = open('file_list','w+')
      for carpeta in carpeta :
          ruta = home +'/'+carpeta
def main():
    check_internet()
if __mame__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
       exit()