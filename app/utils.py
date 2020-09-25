# coding: utf-8

from app.settings import SECRET_KEY
import sys, traceback
from os import system

import subprocess
import threading

def get_trace():
    """
    just to get the traceback of an error
    """
    print("-"*60)
    traceback.print_exc(file=sys.stdout)
    print("-"*60)


def exec_shell(command):
    """
    This method will execute the shell
    
    """
    system(command)
    # p = subprocess.Popen(command.split(),
    #                         shell=True,
    #                         stdout=subprocess.PIPE,
    #                         stderr=subprocess.PIPE)

    # return p.communicate()[0]


def ffmpeg_publish(file_path: str, stream_link: str, stream_key: str):
    """
    This method will try to run the ffmpeg stream
    
    """
    try:
        command = "ffmpeg -i '" + file_path + \
            "' -c:v libx264 -b:v 64k -crf 30 -f flv " + \
            stream_link + "/" + stream_key
        message = "Stream on {} started !".format(stream_link)
        t = threading.Thread(target=exec_shell, args=(command,))
        t.start()

        print("[+] command: ", command)
        print("[+] message: ", message)
        return {
            "status": "success",
            "code": 200,
            "message": message
        }
    except Exception as es:
        get_trace()
        return {
            "status": "error",
            "code": 500,
            "message": "An error occur on the serveur"
        }
