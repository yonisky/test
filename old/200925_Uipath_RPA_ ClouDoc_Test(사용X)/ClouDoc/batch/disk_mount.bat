@echo off
chcp 65001
wmic logicaldisk get name,volumename > C:\RPA_TEST\disk_mount.txt
