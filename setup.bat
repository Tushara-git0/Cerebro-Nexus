@echo off
echo ========================================
echo ResearchPilot AI - Setup Script
echo ========================================
echo.

echo Setting up Backend...
cd backend
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo.
echo Backend setup complete!
echo.
echo IMPORTANT: Edit backend\.env file and add your OpenAI API key
echo.

cd ..
echo Setting up Frontend...
cd frontend
call npm install
echo.
echo Frontend setup complete!
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Add your OpenAI API key to backend\.env
echo 2. Run start_backend.bat in one terminal
echo 3. Run start_frontend.bat in another terminal
echo.
pause
