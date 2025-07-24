@echo on

REM Remove the _build directory if it exists
if exist _build rmdir /s /q _build

REM Run sphinx-apidoc
sphinx-apidoc -F -f -o . ../pyFlightscript/

REM Rename pyFlightscript.rst to index.rst
if exist pyFlightscript.rst rename pyFlightscript.rst index.rst

REM Run make.bat with html parameter
call make.bat html


pause
