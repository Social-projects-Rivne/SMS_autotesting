#Preconditions for test_add_subject_class_for_teacher.txt 
#Author: Vasiluk Dmitry
ssh 5721fe647628e1b5ff000001@smsauto-dvatqc.rhcloud.com <<EOF
mysql < app-root/repo/sql/test_add_subject_class_for_teacher_preparations.sql
EOF
pybot test_add_subject_class_for_teacher.txt
ssh 5721fe647628e1b5ff000001@smsauto-dvatqc.rhcloud.com <<EOF
mysql < app-root/repo/sql/db_init.sql
EOF
