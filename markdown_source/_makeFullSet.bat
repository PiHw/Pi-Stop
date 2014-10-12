@echo off
REM The %%~dpnxF expands to drive, path, basename and extension of the current file.

set TEXTPASER="..\utils\win-textparser\TextParser"
set SRC_PATH="..\markdown_source\markdown"
set TARGET_PATH="..\markdown_generated"


REM List all the source files
for %%F in (%SRCDIR%\*.md) do (
  echo ---Source File: %%~nxF
)

REM Process all the source files
for %%F in (%SRC_PATH%\*.md) do (
  %TEXTPASER% %SRC_PATH:"=%\%%~nxF "output.txt" "<!---,img/,--->" ",IMG_SRC/,"
  .\genFiles.bat %TARGET_PATH:"=%\%%~nxF directorylist.txt
)


pause