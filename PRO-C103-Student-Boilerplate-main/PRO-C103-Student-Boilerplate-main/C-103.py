import sys 
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Lakshmi Ganesh/Downloads"
to_dir = "C:/Users/Lakshmi Ganesh/Downloads/PRO-C103-Student-Boilerplate-main"

dir_tree = {
    "Image_Files":[".png", ".jpg", ".jpeg", ".gif", ".jfif"],
    "Vido_Files":[".mp4", ".mov", ".mpv", ".avi", ".mpg", ".mp2", ".mpeg", ".mpe", ".m4v"],
    "Document_Files":[".doc", "docx", ".txt", ".ppt", ".pdf", ".xsl", ".csv"],
    "Setup_Files":[".exe", ".cmd", ".bin", ".dmg",".msi"]
}

#Event Handler Class

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path)

#Initialize Enent Handler cass

event_handler = FileMovementHandler()
  

#Intialize Observer
observer = Observer()

#Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

#Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")


