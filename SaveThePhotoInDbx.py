import dropbox
import cv2
import os
import time
import random

startTime = time.time()
def TakePic():
    num = random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        ret,frame = videoCaptureObject.read()
        imageName = "image"+str(num)+".png"
        cv2.imwrite(imageName,frame)
        result = False
    return imageName
    videoCaptureObject.release()
    cv2,destroyAllWindows()
    print("photo taken")

def saveImage(ImageName):
    access_token = "sl.A9AUFRUxA9uzZyGxhlJ1ESddcG1lWSVunsRysIVMAF-U6ZF5rAqmTk5vKeWz_aJcOZ9626YMS3Fv17YAHk_SUHfeu6d0hYIwjgkpmy7iwt9o3n5bx_3GFhRzGkmsanKN85tayuPEcDc"
    file_from = ImageName
    file_to = "/picFolder/"+ImageName

    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    whileT = 1
    while whileT<=5:
        if((time.time()-startTime)>=10):
           Time = time.time()
           print('time'+str(Time))
           name = TakePic()
           saveImage(name)
           whileT = whileT+1


main()