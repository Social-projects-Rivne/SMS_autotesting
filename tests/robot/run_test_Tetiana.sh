#Author: Tetiana Kutia

ssh 571fe51b7628e10382000006@django-smstest2.rhcloud.com <<EOF
mysql < app-root/repo/sql/init_db.sql
mysql < app-root/repo/sql/test_data.sql
EOF

pybot test_add_to_school.txt
pybot test_add_class.txt
pybot test_add_topic.txt

ssh 571fe51b7628e10382000006@django-smstest2.rhcloud.com <<EOF
mysql < app-root/repo/sql/init_db.sql
EOF




