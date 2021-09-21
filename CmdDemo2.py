import os
from subprocess import *

# os.system('chcp 65001')
from time import sleep

proc = Popen(
    r'ping 127.0.0.1',
    stdin=None,
    stdout=PIPE,
    stderr=PIPE,
    shell=True
)
print(proc.returncode)
# outinfo, errinfo = proc.communicate()
# outinfo = outinfo.decode('gbk')
# print(outinfo)
while proc.poll()!=0:
    print('doing...')
    sleep(1)
outinfo, errinfo = proc.communicate()
outinfo = outinfo.decode('gbk')
print(outinfo)
print('all ok')
