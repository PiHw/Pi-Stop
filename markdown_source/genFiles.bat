@echo off
REM For info on "for /F" see http://www.computerhope.com/forhlp.htm

set GPP_PATH="..\utils\win-gpp\gpp"
set INC_PATH=".\_inc\"
set TARGET_DIR="..\markdown_generated"

REM Read in the parameters for the target file and the define file
if [%2] == [] (
  set THETARGETFILE=testing.md
) else (
  set THETARGETFILE=%~n1%~x1
)
if [%2] == [] (
  set THEDEFINEFILE=directorylist.txt
) else (
  set THEDEFINEFILE=%2
)
echo Target File:%THETARGETFILE%
echo Define File: %THEDEFINEFILE%


::read %THECSVFILE% and loop through each line
for /F "usebackq eol=; tokens=* delims=" %%A in (%THEDEFINEFILE%) do (
    set the_line=%%A
    call :process_line
)
goto TheEnd

:process_line
for /F "usebackq tokens=1,2,3,4,5,6,7,8,9,10 delims=~" %%1 in ('%the_line:,=~%') do (
    echo Directory: %%~1
    echo Define1:   %%~2
    echo Define2:   %%~3
    echo Define3:   %%~4

    if NOT [%%~1] == [] ( mkdir %TARGET_DIR%\%%~1 )

    %GPP_PATH% -o %TARGET_DIR:"=%\%%~1\%THETARGETFILE% output.txt -I%INC_PATH:"=%\%%~1 %arg1% %arg2% %arg3% %arg4% %arg5% %arg6% %arg7% %arg8%

)


:TheEnd