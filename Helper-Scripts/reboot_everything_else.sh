#!/usr/bin/expect -f
spawn ssh pi@192.168.1.11 "sudo shutdown -r now"
expect "assword:"
send "raspberry\r"
interact

spawn ssh pi@192.168.1.12 "sudo shutdown -r now"
expect "assword:"
send "raspberry\r"
interact

spawn ssh pi@192.168.1.13 "sudo shutdown -r now"
expect "assword:"
send "raspberry\r"
interact