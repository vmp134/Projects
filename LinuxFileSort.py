import os
import shutil

#Dictionary of possible destinations
destination = {
    ".jpg": "/home/victorpeng/Pictures",
    ".jpeg": "/home/victorpeng/Pictures",
    ".heic": "/home/victorpeng/Pictures",
    ".gif": "/home/victorpeng/Pictures",
    ".png": "/home/victorpeng/Pictures",
    ".webp": "/home/victorpeng/Pictures",
    ".avif": "/home/victorpeng/Pictures",

    ".mid": "/home/victorpeng/Music",
    ".midi": "/home/victorpeng/Music",
    ".mp3": "/home/victorpeng/Music",

    ".mp4": "/home/victorpeng/Videos",
    ".mov": "/home/victorpeng/Videos",

    ".docx": "/home/victorpeng/Documents",
    ".pdf": "/home/victorpeng/Documents",
    ".pptx": "/home/victorpeng/Documents",
    ".stl": "/home/victorpeng/Documents",

    ".py": "/home/victorpeng/Documents/Code",
    ".java": "/home/victorpeng/Documents/Code",
    ".c": "/home/victorpeng/Documents/Code"
}

#Actual Sort
def sortDownloads(sourceFolder):
    for filename in os.listdir(sourceFolder):
        extension = os.path.splitext(filename)[1].lower()
        if extension in destination:
            shutil.move(os.path.join(sourceFolder, filename), destination[extension])
        
sortDownloads("/home/victorpeng/Downloads")