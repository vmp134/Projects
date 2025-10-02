import os
import shutil

#Names of locations in case I need to change them quickly

#For Linux
#Root = "/home"
#User = "/victorpeng"

#For Windows
Root = "/home"
User = "/victor"

Pic = "/Pictures"
Aud = "/Music" 
Vid = "/Videos"
Doc = "/Documents"
Cod = "/Code"

#Dictionary of possible destinations
destination = {
    ".jpg": Root + User + Pic,
    ".jpeg": Root + User + Pic,
    ".heic": Root + User + Pic,
    ".gif": Root + User + Pic,
    ".png": Root + User + Pic,
    ".webp": Root + User + Pic,
    ".avif": Root + User + Pic,

    ".mid": Root + User + Aud,
    ".midi": Root + User + Aud,
    ".mp3": Root + User + Aud,

    ".mp4": Root + User + Vid,
    ".mov": Root + User + Vid,

    ".docx": Root + User + Doc,
    ".pdf": Root + User + Doc,
    ".pptx": Root + User + Doc,
    ".stl": Root + User + Doc,
    ".xlsx": Root + User + Doc,

    ".py": Root + User + Doc + Cod,
    ".java": Root + User + Doc + Cod,
    ".c": Root + User + Doc + Cod
}

#Actual Sort
def sortDownloads(Folder):
    for filename in os.listdir(Folder):
        extension = os.path.splitext(filename)[1].lower()
        if extension in destination:
            shutil.move(os.path.join(Folder, filename), destination[extension])
        
sortDownloads("%s%s/Downloads" % (Root, User))