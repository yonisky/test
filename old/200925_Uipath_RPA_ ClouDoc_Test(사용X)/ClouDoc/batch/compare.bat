@echo off
chcp 65001
set scr_path=%1
set des_path=%2
set f_name=%3
fc %scr_path%%f_name% %des_path%%f_name% > C:\RPA_TEST\fc.txt
