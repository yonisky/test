@echo off
chcp 65001
set path=%1
vol %path% > C:\RPA_TEST\disk_label.txt
