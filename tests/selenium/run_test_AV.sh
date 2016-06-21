#Preconditions for test_add_student_selenium.py 
#Author: Alexey Vasiluk

#python test_logout.py
#pylint test_logout.py

ssh 5720427089f5cfbde0000045@ss-alexeyvasiluk.rhcloud.com <<EOF
mysql < app-root/repo/sql/test_add_student_preparations.sql
EOF

#python test_add_student.py
#pylint test_add_student.py

python test_edit_class.py
pylint test_edit_class.py

ssh 5720427089f5cfbde0000045@ss-alexeyvasiluk.rhcloud.com <<EOF
mysql < app-root/repo/sql/db_init.sql
EOF
