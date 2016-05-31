ssh 5730fb8b7628e1b5ba000142@smsautotesting-atqc.rhcloud.com <<EOF
mysql smsautotesting < app-root/repo/sql/smsautotesting_init_db.sql
mysql smsautotesting < app-root/repo/sql/psv_test_search_preparations.sql
EOF
pybot test_search_main_teacher.txt
ssh 5730fb8b7628e1b5ba000142@smsautotesting-atqc.rhcloud.com <<EOF
mysql smsautotesting < app-root/repo/sql/smsautotesting_init_db.sql
EOF




