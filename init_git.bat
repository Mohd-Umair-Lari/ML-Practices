@echo off
echo Initializing Git repository...
git init

echo.
echo Installing Git LFS...
git lfs install

echo.
echo Adding files and committing...
git add .gitattributes
git add .
git commit -m "Initial commit with large files tracked via Git LFS"

echo.
echo Setting main branch...
git branch -M main

echo.
echo Adding remote origin...
git remote add origin https://github.com/Mohd-Umair-Lari/ML-Practices.git

echo.
echo Pushing to remote...
git push -u origin main

echo.
echo Done!
pause
