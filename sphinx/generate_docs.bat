@echo on

REM Remove the _build directory if it exists
if exist _build rmdir /s /q _build

REM Run sphinx-apidoc
sphinx-apidoc -o . ../pyFlightscript/

REM Rename pyFlightscript.rst to index.rst
if exist pyFlightscript.rst rename pyFlightscript.rst index.rst

REM Run make.bat with html parameter
call make.bat html

REM Copy and replace index.html two folder levels up
if exist .\_build\html\ copy /Y .\_build\html\* ..\docs\

REM Inform user of the location of docs
echo docs are in .\_build\html\index.html

pause
