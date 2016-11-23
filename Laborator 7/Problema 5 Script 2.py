import os
import json
import time
import zipfile

def selectFILES(all_files):
    selected_files = list()
    for iterator in all_files:
        try:
            if os.path.isfile(iterator)==False:
                raise Exception("Not a file")
            else:
                size = os.path.getsize(iterator)
                last_modified = os.stat(iterator).st_mtime

                last_modified_time=time.time() - last_modified
                if size <= 102400 and  last_modified_time<= 5 * 60:
                    selected_files.append(iterator)
        except:
            pass


    return selected_files


def archive_files():
    data = open("D:\\a.txt", "rt").read()
    all_files = json.loads(data)

    selectedFiles = selectFILES(all_files)


    ziper=zipfile.ZipFile("newzip.zip","w",zipfile.ZIP_DEFLATED)

    for iterator in selectedFiles:
        ziper.write(iterator)
    ziper.close()



archive_files()
