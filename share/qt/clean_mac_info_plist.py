#!/usr/bin/env python
# Jonas Schnelli, 2013
# make sure the Bitcoin-Qt.app contains the right plist (including the right version)
# fix made because of serval bugs in Qt mac deployment (https://bugreports.qt-project.org/browse/QTBUG-21267)

from string import Template
from datetime import date
import os

bitcoin_directory =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
version = "unknown"


''' If the output folder doesn't exists? create it.'''
output_directory = "Bitcoin-Qt.app/Contents"
if not os.path.exists(output_directory):
	os.makedirs(output_directory)

output_file = os.path.join(output_directory,"Info.plist")
input_file = os.path.join(bitcoin_directory,'share/qt/Info.plist')

''' To grab the version number from the dimecoin-qt.pro file and store in the version variable '''
file_for_grabbing_version = os.path.join(bitcoin_directory,"dimecoin-qt.pro")
for line in open(file_for_grabbing_version):
	lineArr = line.replace(" ", "").split("=")
	if lineArr[0].startswith("VERSION"):
		version = lineArr[1].replace("\n", "")

with open(input_file,'r') as input_file:
	file_content = input_file.read()
	string_ = Template(file_content)
	new_file_contents = string_.substitute(VERSION=version,YEAR=date.today().year)

with open(output_file,'w') as output_file:
	output_file.write(new_file_contents)
	
print "Info.plist fresh created"