@echo off
set /p SOURCE_DIR_NAME="Enter the source directory name: "
set SOURCE_PATH=D:\Python\Examples\%SOURCE_DIR_NAME%

set /p DIR_NAME="Enter the directory name: "
set DESTINATION_PATH=D:\cadwork\userprofil_30\3d\API.x64\%DIR_NAME%

echo Copying folders and .py files...

xcopy /s /i /y "%SOURCE_PATH%\*.py" "%DESTINATION_PATH%\"
xcopy /s /i /y "%SOURCE_PATH%\*.json" "%DESTINATION_PATH%\"

echo Copy complete.