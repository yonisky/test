@echo off
set drive=%1
set des_path=%2
%drive%
cd %des_path%
start notepad++