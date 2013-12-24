del MANIFEST
rmdir /S /Q build
rmdir /S /Q dist
python setup.py build sdist
pause