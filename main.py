#!/usr/bin/env python

__author__ = 'Igor Maculan <n3wtron@gmail.com>'
import logging
import sys
sys.path.insert(0, '/pushbullet_lib')

from pushbullet import Listener
from pushbullet import Pushbullet
import webbrowser


logging.basicConfig(level=logging.ERROR)
key_file = open('api/pushbullet_key', 'r')
API_KEY = key_file.readline().rstrip()
key_file.close()

HTTP_PROXY_HOST = None
HTTP_PROXY_PORT = None



def on_push(data):
    pushes = pb.get_pushes()
    latest_push = pushes[0]['body'].split(':')
    command = latest_push[0]
    extra_info = latest_push[1].strip().split(' ')
    command_dict[command](extra_info)



def turn_on(device):
    print("turning on device")

def turn_off(device):
     print("turning off device")

def open(text):
    print("opening..")
    if text[0].strip().lower() == "youtube":
        webbrowser.open('http://youtube.com', new=2)

command_dict = {"turn on": turn_on, "turn off": turn_off, "open": open}

pb = Pushbullet(API_KEY)
pb.delete_pushes()
def main():


    s = Listener(account=pb,
                 on_push=on_push,
                 http_proxy_host=HTTP_PROXY_HOST,
                 http_proxy_port=HTTP_PROXY_PORT)
    try:
        s.run_forever()
    except KeyboardInterrupt:
        s.close()


if __name__ == '__main__':
    main()