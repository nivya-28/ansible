import subprocess
f = open('filename.txt','r')
x = f.readlines()
i = 0
while i < len(x):
    print(x[i])
    subprocess.call("ansible-playbook % s" %x[i],shell = True)
    i = i+1
