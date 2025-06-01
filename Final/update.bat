@echo off

rem	If you can read this, 
rem	please email etreed@students.unwsp.edu
rem	saying "Fuzzy Pickles."
rem	That would be most kind, thank you.

call auto.bat
git add README.md
git add auto.bat
git add update.bat
git add *.py
git add *.db
git commit -m "Made changes"
git push
