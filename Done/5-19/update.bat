@echo off
call auto.bat
git add README.md
git add auto.bat
git add update.bat
git add main.py
git commit -m "Made changes"
git push
