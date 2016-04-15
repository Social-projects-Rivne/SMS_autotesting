# School management system #
School management system is an application that provides ability to manage schools of a city. 

### Version
1.0.3

### Installation
For installing required libs and frameworks execute next commands:
```sh
    git clone git@bitbucket.org:Michaluch/rv-010.python.git
    sudo apt-get install build-essential python-dev libmysqlclient-dev
    sudo apt-get install libjpeg-dev
    pip install -r requirements.txt
```

Next step you need to create CONF.ini file in 'configurations' folder on one level as the project.
CONF.ini should contain next lines with yours setting:

    [DataBase]
    ENGINE = django.db.backends.mysql
    HOST = localhost
    USER = root
    PASSWORD = password
    NAME = SMSDB

    [SMTP]
    ADMIN_EMAIL = example@gmail.com
    EMAIL_HOST = smtp.mandrillapp.com
    EMAIL_PORT = 587
    EMAIL_HOST_USER = second_example@gmail.com
    EMAIL_HOST_PASSWORD = host_password
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

    [Logs]
    USE_LOGS = True
    TRACK_USERS = True
    USE_CUSTOM_LOG_DIR = False
    CUSTOM_LOG_DIR = /var/log/SMS

There are a few toggling log variables which lets us configurate project logs:

  - You can turn logs on `USE_LOGS = True` with such paramether.

  - `TRACK_USERS = True` lets us to log every user's request.

  - If you want to change logs locating - set: `USE_CUSTOM_LOG_DIR = True`, and assign full path to your directory in
`CUSTOM_LOG_DIR = /etc/log/SMS`. Not forget to give `write` permission for log folder.

#### Fixtures
In case you want to fill necessary data of system into database execute next command:
```sh
    mysql -u root -p SMSDB < SMS/utils/sql_scripts/fill_db.sql
```
If you just want to fill test_data into database execute next command:
```sh
    mysql -u root -p SMSDB < fixture/test_data.sql
```

License
----
BSD