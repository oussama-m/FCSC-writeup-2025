import subprocess

all_path = subprocess.Popen('grep -rs "@icloud.com" --exclude="find_icloud.py"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in all_path.stdout.readlines():
    path = "strings ./"+str(line).replace("b'grep: ", "").replace("binary file matches\\n'", "")[:-2]+" | grep 'icloud.com'"
    # print(path)
    all_account = subprocess.Popen(path, shell=True)