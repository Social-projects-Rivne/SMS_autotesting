#Preconditions for test_add_subject_class_for_teacher.txt 
#Author: Vasiluk Dmitry
ssh 5721fe647628e1b5ff000001@smsauto-dvatqc.rhcloud.com <<EOF
mysql < app-root/repo/sql/test_school_crud_preparations.sql
EOF
pybot test_school_crud.txt
ssh 5721fe647628e1b5ff000001@smsauto-dvatqc.rhcloud.com <<EOF
mysql < app-root/repo/sql/db_init.sql
EOF
