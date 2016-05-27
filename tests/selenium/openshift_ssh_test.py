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

# stdin, stdout, stderr = client.exec_command('ls')
# for line in stdout.readlines():
#     print (str(line).strip())

stdin, stdout, stderr = client.exec_command('echo $OPENSHIFT_MYSQL_DB_URL$')
out_str = str(stdout.readlines()[0]).strip()

# mysql_host = "127.11.47.2"
# mysql_login = "adminMK8EU2A"
# mysql_password = "kdfQxfCWtZaq"

database_name = "sms"

host = out_str[out_str.index("@")+1:]
mysql_host = host[:host.index(":")]

login = out_str[out_str.index("//")+2:]
mysql_login = login[:login.index(":")]

password = out_str[out_str.index(":")+1:]
mysql_password = password [password .index(":")+1:password .index("@")]

# sql_expression = "INSERT INTO Teachers (school_id, id, name, role_id, login, email, password, state, avatar, salt) VALUES " \
#                  "(NULL, 5555, '\xD0\xA1\xD0\xB5\xD0\xBC\xD0\xB8\xD1\x89\xD0\xB5\xD0\xBD\xD0\xBA\xD0\xBE\x20\xD0\xA5\xD1\x80\xD0\xB8\xD1\x81\xD1\x82\xD0\xBE\xD1\x84\xD0\xBE\xD1\x80\x20\xD0\x9E\xD0\xBD\xD1\x83\xD1\x84\xD1\x80\xD1\x96\xD0\xB9\xD0\xBE\xD0\xB2\xD0\xB8\xD1\x87', 1, 'semuschenko', 'semuschenko@gmail.com', 'pDk7jf', 1, NULL, NULL);"

sql_expression = "\"INSERT INTO Teachers (school_id, id, name, role_id, login, email, password, state, avatar, salt) VALUES " \
                  "(NULL, 77777, 'Семищенко Христофор Онуфрійович', 1, 'semuschenko', 'semuschenko@gmail.com', 'pDk7jf', 1, NULL, NULL);\""

command_line = "mysql -D {db} -h {host} -u {uname} --password={passwd} --execute=\"{sql}\"".format(
    db = database_name, host = mysql_host, uname =  mysql_login, passwd = mysql_password, sql = sql_expression)
# command_line = "mysql -D {db} --execute=\"{sql}\"".format(db = database_name, uname =  mysql_login, passwd = mysql_password, sql = sql_expression)
# command_line = "mysql -D {db} -h {host} -u {uname} --password={passwd} --execute=\"{sql}\"".format(
#     db = database_name, host = mysql_host, uname =  mysql_login, passwd = mysql_password, sql = "select * from Teachers;")

command_line = " echo {} > /tmp/1.sql".format(sql_expression)
# print(command_line)
stdin, stdout, stderr = client.exec_command(command_line.decode("utf-8"))

command_line = "mysql -D {db} -h {host} -u {uname} --password={passwd} < /tmp/1.sql".format(
    db = database_name, host = mysql_host, uname =  mysql_login, passwd = mysql_password, )

stdin, stdout, stderr = client.exec_command(command_line.encode("utf-8"))

locale = [
"LANG=\"en_US.UTF-8\"",
"LC_CTYPE=\"en_US.UTF-8\"",
"LC_NUMERIC=\"en_US.UTF-8\"",
"LC_TIME=\"en_US.UTF-8\"",
"LC_COLLATE=\"en_US.UTF-8\"",
"LC_MONETARY=\"en_US.UTF-8\"",
"LC_MESSAGES=\"en_US.UTF-8\"",
"LC_PAPER=\"en_US.UTF-8\"",
"LC_NAME=\"en_US.UTF-8\"",
"LC_ADDRESS=\"en_US.UTF-8\"",
"LC_TELEPHONE=\"en_US.UTF-8\"",
"LC_MEASUREMENT=\"en_US.UTF-8\"",
"LC_IDENTIFICATION=\"en_US.UTF-8\""]

for l in locale:
    stdin, stdout, stderr = client.exec_command("export " + l)
    for line in stdout.readlines():
      print (str(line).strip().encode("utf-16"))



stdin, stdout, stderr = client.exec_command("export LANGUAGE=\"en\"")

stdin, stdout, stderr = client.exec_command("export LANG=\"C\"")

stdin, stdout, stderr = client.exec_command("export LC_MESSAGES=\"C\"")

stdin, stdout, stderr = client.exec_command("locale")

for line in stdout.readlines():
    print (str(line).strip().encode("utf-16"))

for line in stderr.readlines():
    print (str(line).strip())

client.close()

# stdin, stdout, stderr = client.exec_command('ls -l')
# data = stdout.read() + stderr.read()
# client.close()"