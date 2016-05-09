#rhc port-forward sms &
#rhc app-stop sms
sleep 10
mysql -u adminMK8EU2А --port=3307 --host=127.0.0.1 --password=kdfQxfCWtZаq < sms.sql
#rhc app-restart sms
