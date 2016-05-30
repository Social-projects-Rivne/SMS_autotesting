#preparation for running tests for "set mark" option on RobotFramework
#by Sebestyanovych A.
ssh 5730fb8b7628e1b5ba000142@smsautotesting-atqc.rhcloud.com <<EOF
mysql < app-root/repo/sql/smsautotesting_init_db.sql
mysql < app-root/repo/sql/set_mark.sql
EOF
pybot test_set_mark.txt
ssh 5730fb8b7628e1b5ba000142@smsautotesting-atqc.rhcloud.com <<EOF
mysql < app-root/repo/sql/smsautotesting_init_db.sql
EOF
