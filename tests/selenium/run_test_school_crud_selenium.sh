#Preconditions for test_school_crud.py 
#Author: Vasiluk Dmitry
ssh 5721fe647628e1b5ff000001@smsauto-dvatqc.rhcloud.com <<EOF
mysql < app-root/repo/sql/test_school_crud_preparations.sql
EOF
python test_school_crud_selenium.py 
ssh 5721fe647628e1b5ff000001@smsauto-dvatqc.rhcloud.com <<EOF
mysql < app-root/repo/sql/db_init.sql
EOF
pylint test_school_crud_selenium.py
