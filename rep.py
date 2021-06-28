#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
import subprocess
cmd = cgi.FieldStorage()
cont=cmd.getvalue("y")
rep=cmd.getvalue("z")
reps=subprocess.getoutput('sudo kubectl scale  --replicas=' +rep + " " ' deployment/'  +cont + ' --kubeconfig /root/TASK_9/admin.conf')

print("Your replica created  Successfully Launch : " +reps)

