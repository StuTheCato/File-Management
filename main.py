import shutil, os
import time
from time import sleep

source_dir = "C:/Users/spons/Downloads"
target_dir_img = "C:/Users/spons/Pictures"
target_dir_video  = "C:/Users/spons/Videos"
target_dir_audio = "C:/Users/spons/Music"
target_dir_setup = "C:/Users/spons/Downloads/Setup"
target_dir_rar = "C:/Users/spons/Downloads/rar"

def manage_files():
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        if file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg"):
            shutil.move(source_dir + "/" + file_name, target_dir_img)
        elif file_name.endswith(".mp4") or file_name.endswith(".mkv"):
            shutil.move(source_dir + "/" + file_name, target_dir_video)
        elif file_name.endswith(".mp3"):
            shutil.move(source_dir + "/" + file_name, target_dir_audio)
        elif file_name.endswith(".exe"):
            shutil.move(source_dir + "/" + file_name, target_dir_setup)
        elif file_name.endswith(".rar") or file_name.endswith(".zip"):
            shutil.move(source_dir + "/" + file_name, target_dir_rar)

manage_files()
sleep(3)
print("All files are moved to their respective folders.")