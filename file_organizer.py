import os
from time import sleep

EXTENSIONS = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma",".oac",".aup"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"],
    "SHORTCUTS": [".lnk",".url"],
    "INSTALLERS": [".msi",".oiv",".OIV",".apk"]
}

def organize(PATH):
    try:
        FILES = os.listdir(PATH)
    except Exception as e:
        print(str(e))
        print("Failed to locate path. Exiting...")
        sleep(5)
        quit()
    FILE_EXTENSIONS = []
    for i in range(len(FILES)):
        FILE_EXTENSIONS.append(os.path.splitext(PATH+FILES[i])[1])
        print(FILE_EXTENSIONS[i])
    for i in range(len(FILE_EXTENSIONS)):
       for j in EXTENSIONS:
           if FILE_EXTENSIONS[i] in EXTENSIONS[j]:
               print(f"Extension found: {FILE_EXTENSIONS[i]} in  {j}")
               create_directory(PATH,j)
    for f in FILES:
        ext = os.path.splitext(PATH+f)[1]
        print(f"File: {f} Extension: {ext}")
        for j in EXTENSIONS:
            if ext in EXTENSIONS[j]:
                print(f"File: {f} Extension: {ext} belongs in Folder: {j}")
                os.rename(PATH+"\\"+f,PATH+"\\"+j+"\\"+f)
    print("Directory organized. Exiting...")
    sleep(5)

def create_directory(PATH, DIRNAME):
    try:
        os.mkdir(PATH+"\\"+DIRNAME)
    except FileExistsError:
        print(f"Directory: {DIRNAME} already exists.. Moving on")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    print("Welcome to the File Organizer.\nCreated by: Darren Shaw")
    print("Directory to organize:\n")
    PATH = input()
    organize(PATH)
