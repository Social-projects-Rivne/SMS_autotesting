#Author: Tetiana Kutia

#Author: Tetiana Kutia

ssh 571fe51b7628e10382000006@django-smstest2.rhcloud.com <<EOF
mysql < app-root/repo/sql/init_db.sql
mysql < app-root/repo/sql/test_data.sql
EOF

python test_add_to_school.py
python test_add_class.py
python test_add_topic.py

ssh 571fe51b7628e10382000006@django-smstest2.rhcloud.com <<EOF
mysql < app-root/repo/sql/init_db.sql
EOF




