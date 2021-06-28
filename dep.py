#!/usr/bin/python3
print("content-type: text/html")
print()


import cgi
import subprocess
cmd = cgi.FieldStorage()
img=cmd.getvalue("x")
cont=cmd.getvalue("d")
out=subprocess.getoutput('sudo kubectl create deployment ' +cont + ' --image='+img+ ' --kubeconfig /root/TASK_9/admin.conf')
print("Your  Deployment  Successfully Launched : " +out)

