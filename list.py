#!/usr/bin/python3

import cgi
import subprocess


print("content-type: text/html")
print()

mydata = cgi.FieldStorage()


output = subprocess.getoutput(" sudo kubectl get pods --kubeconfig /root/TASK_9/admin.conf")

print(output)

