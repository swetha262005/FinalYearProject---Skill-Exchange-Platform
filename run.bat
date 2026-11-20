@echo off
echo =========================================
echo   LearnMate - Skill Exchange Platform   
echo =========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo Starting LearnMate application...
echo Access the application at: http://127.0.0.1:5000
echo.
echo Default Admin Credentials:
echo Username: admin
echo Password: admin123
echo.
echo Press Ctrl+C to stop the server
echo =========================================
echo.

REM Run the application
python app.py

pause
