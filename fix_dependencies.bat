@echo off
echo ========================================
echo Fixing NumPy and Package Dependencies
echo ========================================

echo Step 1: Uninstalling problematic packages...
pip uninstall numpy scipy scikit-learn pandas thinc spacy -y

echo Step 2: Installing NumPy 1.24.3...
pip install numpy==1.24.3 --no-deps

echo Step 3: Installing compatible SciPy...
pip install scipy==1.10.1

echo Step 4: Installing scikit-learn...
pip install scikit-learn==1.3.0

echo Step 5: Installing pandas...
pip install pandas==2.0.3

echo Step 6: Installing other packages...
pip install flask python-docx pypdf2 nltk textblob

echo Step 7: Removing conflicting packages...
pip uninstall thinc spacy cymem preshed blis -y

echo.
echo ========================================
echo Dependencies Fixed!
echo ========================================
echo Verifying installation...
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"
python -c "import sklearn; print(f'Scikit-learn: {sklearn.__version__}')"
python -c "import pandas; print(f'Pandas: {pandas.__version__}')"
echo ========================================
pause