@echo off
echo Building Python Descomplicado with Quarto...

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if needed
echo Installing Python dependencies...
pip install -r docs/requirements.txt

REM Build the book
echo Building book...
cd docs
quarto render

REM Open the book in browser
echo Opening book in browser...
quarto preview

cd ..
echo Build complete!
pause
