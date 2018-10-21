## Program rekursywnie skanujący system plików 
# w poszukiwaniu zdjęć zapisanych w formacie .jpg
# następnie modyfikujący ich rozdzielczość o zadany procent
#
# Przyjmuje następujące argumenty:
# > resize.py [ścieżka do skanowanego katalogu] [procent zmiany rozdzielczości]
#
import os
import subprocess
import sys

hello = "\n#   Hubert Weydmann\n# Program rekursywnie skanujący system plików \n# w poszukiwaniu zdjęć zapisanych w formacie .jpg\n# następnie modyfikujący ich rozdzielczość o zadany procent\n#\n# Przyjmuje następujące argumenty:\n# > resize.py [ścieżka do skanowanego katalogu] [procent zmiany rozdzielczości]"

def resize(arguments):
    working_dir = ""
    percentage = ""
    # upewnij się co do ilości argumentów
    if len(arguments) == 1 or len(arguments) > 3:
        print(hello)
        return 1

    if len(arguments) >= 2:
        working_dir = arguments[1]

    if len(arguments) >= 3:
        percentage = arguments[2]
    
    files = []
    processes_list = []

    # search(working_dir, percentage, processes_list)
    search_files(working_dir, files)
    for f in files:
        p = mogrify(f, percentage)
        processes_list.append(p)
        print("Running process for: " + f + ", PID: ", p.pid)
    for p in processes_list:
        p.terminate()
    return 0

def mogrify(filepath, _percentage):
    command = "magick mogrify -resize " + _percentage + " \"" + os.path.abspath(filepath) + "\""
    theproc = subprocess.Popen(command, shell = True)
    return theproc
    

def search_files(dir_path, path_list):
    if os.path.isdir(dir_path):
        for p in os.listdir(dir_path):
            search_files(os.path.join(dir_path, p), path_list)
    elif dir_path.endswith(".jpg"):
        path_list.append(os.path.abspath(dir_path))

if __name__ == "__main__": resize(sys.argv)
