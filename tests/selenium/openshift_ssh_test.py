# -*- coding: utf-8 -*-
"""  _  """
import paramiko


# ssh://5717dd130c1e6612d4000085@sms-rv016atqc.rhcloud.com/~/git/sms.git/
host = "sms-rv016atqc.rhcloud.com" #/~/git/sms.git/
user = "5717dd130c1e6612d4000085"
port = 22
key = 'keys/id_rsa'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, port=port, key_filename=key)
#
# client.connect('<hostname>', username='<username>', password='<password>', key_filename='<path/to/openssh-private-key-file>')

stdin, stdout, stderr = client.exec_command('ls')
print stdout.readlines()
client.close()

# stdin, stdout, stderr = client.exec_command('ls -l')
# data = stdout.read() + stderr.read()
# client.close()