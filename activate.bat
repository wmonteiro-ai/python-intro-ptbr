@echo off
echo Activating Python virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated!
echo.
echo You can now run:
echo   cd docs
echo   quarto render
echo   quarto preview
echo.
cmd /k


