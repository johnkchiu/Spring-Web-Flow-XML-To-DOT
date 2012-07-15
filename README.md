Spring-Web-Flow-XML-To-DOT
==========================

Creates a DOT file from a Spring Web Flow XML file.  It only supports Spring Web
Flow 2.0 XML file format.  The script writes to console, so you can be easily 
piped to file.

To view the DOT file, you can use something like Graphviz - http://graphviz.org.

Installation
============
To use it, just download the script.  Make it executable, and then use it.
```
$ wget https://raw.github.com/johnkchiu/Spring-Web-Flow-XML-To-DOT/master/springWebFlowXmlToDot.py
$ chmod a+x springWebFlowXmlToDot.py
```

Usage
=====
```
usage: springWebFlowXmlToDot.py [-h] -f FILENAME [-v]

Generates a DOT file from a Spring Web Flow XML file

optional arguments:
  -h, --help   show this help message and exit
  -f FILENAME  Spring Web Flow XML file
  -v           show program's version number and exit
```