: outfile - output file name and path
: renderer - output file type (test, html, json)
@echo off
pyinstrument --outfile="./profile.html" --renderer="html"  ../project_file/main_project.py