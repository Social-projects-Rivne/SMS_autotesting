"""
SSH Test preparation template
"""

import paramiko


# ssh 5730fb8b7628e1b5ba000142@smsautotesting-atqc.rhcloud.com
_hostname = "smsautotesting-atqc.rhcloud.com"
_port = 22
_username = "5730fb8b7628e1b5ba000142"

# ssh commands
_cmd_dump = "mysqldump smsautotesting -h $OPENSHIFT_MYSQL_DB_HOST " \
            "-P ${OPENSHIFT_MYSQL_DB_PORT:-3306} " \
            "-u ${OPENSHIFT_MYSQL_DB_USERNAME:-'admin'} " \
            "--password=\"$OPENSHIFT_MYSQL_DB_PASSWORD\" " \
            "--default-character-set=utf8 > " \
            "~/app-root/repo/sql/db_backup.sql;"
_cmd_restore = "mysql smsautotesting -h $OPENSHIFT_MYSQL_DB_HOST " \
               "-P ${OPENSHIFT_MYSQL_DB_PORT:-3306} " \
               "-u ${OPENSHIFT_MYSQL_DB_USERNAME:-'admin'} " \
               "--password=\"$OPENSHIFT_MYSQL_DB_PASSWORD\" " \
               "--default-character-set=utf8 < " \
               "~/app-root/repo/sql/db_backup.sql;"
_cmd_sql = "mysql smsautotesting -h $OPENSHIFT_MYSQL_DB_HOST " \
           "-P ${OPENSHIFT_MYSQL_DB_PORT:-3306} " \
           "-u ${OPENSHIFT_MYSQL_DB_USERNAME:-'admin'} " \
           "--password=\"$OPENSHIFT_MYSQL_DB_PASSWORD\" " \
           "--default-character-set=utf8 < " \
           "~/app-root/repo/sql/"


def prepare_db(action='setup', sql_filename='smsautotesting_init_db.sql'):
    """
    Method to make test preparation template action
    on cloud through ssh connection using paramiko library
    """

    try:
        max_size = 120 * 1024 * 1024
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=_hostname,
                           port=_port,
                           username=_username,
                           key_filename='id_rsa', timeout=10)
            print("ssh connection established successfully (" +
                  action + ")")
        except (paramiko.BadHostKeyException,
                paramiko.AuthenticationException,
                paramiko.SSHException) as ex:
            print("Error while connecting through ssh: " + str(ex.message))
            raise
        except Exception as ex:
            print("Some Error occurred in ssh: " + str(ex.message))
            raise

        channel = client.get_transport().open_session()
        channel.settimeout(100)

        if action == 'setup':
            channel.exec_command(_cmd_dump +
                                 _cmd_sql + sql_filename)
        else:
            channel.exec_command(_cmd_restore)

        content = ""
        data = channel.recv(1024)
        # Capturing data from channel buffer.
        while data:
            content += data
            data = channel.recv(1024)
        status, response, error = channel.recv_exit_status(), content, \
                                  channel.recv_stderr(max_size)
        client.close()
        final_output = unicode(response) + unicode(error)
        # message = ''
        if action == 'setup':
            message = 'Test preparation executed.'
        else:
            message = 'Database restored.'
        print([message, status, final_output])
    except Exception as ex:
        print("SSH operation exception occurred (" + action + "): " +
              str(ex.message))
        raise

