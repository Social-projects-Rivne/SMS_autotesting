ssh 5730fb8b7628e1b5ba000142@smsautotesting-atqc.rhcloud.com <<EOF
mysql smsautotesting < app-root/repo/sql/smsautotesting_init_db.sql
mysql smsautotesting < app-root/repo/sql/psv_test_change_avatar_preparations.sql
EOF
pybot sms_autotesting_avatar_change.txt
ssh 5730fb8b7628e1b5ba000142@smsautotesting-atqc.rhcloud.com <<EOF
mysql smsautotesting < app-root/repo/sql/smsautotesting_init_db.sql
EOF




