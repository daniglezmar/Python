SecPoint.com Google Penetration Testing Hack Database v 1.0

Database of Google Hacks and a tool for manipulating it. 
Database is separated to files by categories. You could use DB alone, or 
use the tool to analyse your own site by adding site search option
to all queries. 

This tool will take source file (file with a list of queries) and generate 
website-specific queries (-s option) by adding site:sitename.com to each
query. 

run as
./googleDB-tool.py <source file> <options>

   <source file>        queries source file from GoogleDB (files in db directory)

Options are:
    -o output.txt       save output to file
    -s sitename.com     generate queries for this site only


Example:

./googleDB-tool.py "login_pages.txt"  -o file.html -s site.com

will generate list of queries for finding login pages
on site.com and save report to "file.html"

History: 
# ## 1.0 initial release