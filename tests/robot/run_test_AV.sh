#Preconditions for test_add_student_selenium.py 
#Author: Alexey Vasiluk

pybot test_logout.txt 

ssh 5720427089f5cfbde0000045@ss-alexeyvasiluk.rhcloud.com <<EOF
mysql < app-root/repo/sql/test_add_student_preparations.sql
EOF

pybot test_add_student.txt
pybot test_edit_class.txt

ssh 5720427089f5cfbde0000045@ss-alexeyvasiluk.rhcloud.com <<EOF
mysql < app-root/repo/sql/db_init.sql
EOF
