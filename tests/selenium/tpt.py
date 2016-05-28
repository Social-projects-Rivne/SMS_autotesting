""" SSH Test preparation template"""

import paramiko


class TestPrepTemplate(object):

    """ Class implements static method to
    make test preparation template action on cloud through ssh connection
    """

    # ssh 5730fb8b7628e1b5ba000142@smsautotesting-atqc.rhcloud.com
    _hostname = "smsautotesting-atqc.rhcloud.com"
    _port = 22
    _username = "5730fb8b7628e1b5ba000142"

    # ssh commands
    _cmd_dump = "mysqldump smsautotesting -h $OPENSHIFT_MYSQL_DB_HOST " \
                "-P ${OPENSHIFT_MYSQL_DB_PORT:-3306} " \
                "-u ${OPENSHIFT_MYSQL_DB_USERNAME:-'admin'} " \
                "--password=\"$OPENSHIFT_MYSQL_DB_PASSWORD\" > " \
                "~/app-root/repo/sql/db_backup.sql;"
    _cmd_restore = "mysql smsautotesting -h $OPENSHIFT_MYSQL_DB_HOST " \
                   "-P ${OPENSHIFT_MYSQL_DB_PORT:-3306} " \
                   "-u ${OPENSHIFT_MYSQL_DB_USERNAME:-'admin'} " \
                   "--password=\"$OPENSHIFT_MYSQL_DB_PASSWORD\" < " \
                   "~/app-root/repo/sql/db_backup.sql;"
    _cmd_sql = "mysql smsautotesting -h $OPENSHIFT_MYSQL_DB_HOST " \
               "-P ${OPENSHIFT_MYSQL_DB_PORT:-3306} " \
               "-u ${OPENSHIFT_MYSQL_DB_USERNAME:-'admin'} " \
               "--password=\"$OPENSHIFT_MYSQL_DB_PASSWORD\" < " \
               "~/app-root/repo/sql/"

    @staticmethod
    def prepare_db(action='setup', sql_filename='smsautotesting_init_db.sql'):
        try:
            max_size = 120 * 1024 * 1024
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(hostname=TestPrepTemplate._hostname,
                               port=TestPrepTemplate._port,
                               username=TestPrepTemplate._username,
                               key_filename='id_rsa', timeout=10)
            except (paramiko.BadHostKeyException,
                    paramiko.AuthenticationException,
                    paramiko.SSHException) as e:
                return e
            except BaseException as e:
                return "General exception: " + e

            channel = client.get_transport().open_session()
            channel.settimeout(100)

            if action == 'setup':
                channel.exec_command(TestPrepTemplate._cmd_dump +
                                     TestPrepTemplate._cmd_sql + sql_filename)
            elif action == 'teardown':
                channel.exec_command(TestPrepTemplate._cmd_restore)

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
            return [status, final_output]
        except Exception as e:
            return [1, unicode(e)]

