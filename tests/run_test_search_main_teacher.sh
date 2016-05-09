ssh 572956f60c1e66323d0001c6@smscloud-psvatqc.rhcloud.com <<EOF
mysql < app-root/repo/create_test_db.sql
cp app-root/repo/wsgi/configurations/conf_test app-root/repo/wsgi/configurations/CONF.ini
EOF
pybot test_search_main_teacher.txt
ssh 572956f60c1e66323d0001c6@smscloud-psvatqc.rhcloud.com <<EOF
mysql < app-root/repo/drop_test_db.sql
cp app-root/repo/wsgi/configurations/conf_origin app-root/repo/wsgi/configurations/CONF.ini
EOF
