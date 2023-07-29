import subprocess

USER_FOLDER = "/home/parallels"
FILE = "file.txt"
TST_FOLDER = "tst"
OUT_FOLDER = "out"
FOLDER_FOLDER = "folder1"
TEXT_OK = "Everything is Ok"
TEXT_FAIL = "Is not archive"
TEXT_HEADERS_ERROR = "Headers Error"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout and result.returncode == 0) or text in result.stderr:
        return True
    else:
        return False
