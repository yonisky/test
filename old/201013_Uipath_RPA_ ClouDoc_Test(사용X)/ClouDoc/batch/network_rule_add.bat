@echo off
netsh advfirewall firewall add rule name="ClouDoc" dir=out action=block remoteip="192.168.1.183" enable=no