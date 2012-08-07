#!/usr/bin/env python
#
# Copyright (c) 2012 by John Chiu
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# --- Change Log ---------------------------------------------------
# 0.2
#	- Added support for decision-state
# 0.1 
#	- Changed shape/color, and added an example.
#	- Add initial working file.
# ------------------------------------------------------------------

__author__ = 'johnkchiu@yahoo.com (John Chiu)'
__version__ = '0.2'


import argparse
import xml.sax

def writeGraphStart(graphName):
	print 'digraph "' + graphName + '" {'
	print

def writeGraphEnd():
	print '}'

def writeStartState(startState):
	print '\t// Start state';
	print '\t"Start" [label="Start", fontname="Helvetica", shape="circle", style="filled", fillcolor="green"];'
	print '\t"Start" -> "' + startState + '";'
	print

def writeEndState():
	print '\t// End state'
	print '\t"End" [label="End", fontname="Helvetica", shape="circle", style="filled", fillcolor="red"];'

def writeState(name, id, transitions):
	# set fillColor & shipe
	if name == 'subflow-state':
		fillcolor = 'gray'
		shape = 'rectangle'
	elif name == 'view-state':
		fillcolor = 'lightblue'
		shape = 'rectangle'
	elif name == 'decision-state':
		fillcolor = 'white'
		shape = 'diamond'
	else :
		fillcolor = 'white'
		shape = 'oval'
	# write state info
	print '\t // ' + name + ' (' + id + ')'
	print '\t"' + id + '" [label="' + id + '", fontname="Helvetica", shape="' + shape + '", style="filled", fillcolor="' + fillcolor + '", width="2.5", height="1"];'
	# write state transitions
	if len(transitions) > 0 :
		for transition in transitions:
			print '\t"' + id + '" -> "' + transition['to'] + '" [label="' + transition['on'] + '", fontname="Helvetica"];'
	else :
		print '\t"' + id + '" -> "End"' 
	print

# Class for handling the parsing of the Spring XML format
class SpringXmlHandler(xml.sax.ContentHandler):
	def __init__ (self):
		self.isFirstState = True
		self.id = ''
		self.transition = {}
		self.transitions = []

	def startElement(self, name, attributes):
		# if name == 'flow':
		# 	writeStartState(attributes.getValue('start-state'))
		# el
		if name in ('action-state', 'view-state', 'decision-state', 'subflow-state', 'end-state'):
			self.id = attributes.getValue('id')
		elif name == 'transition':
			# iterate thru attributes and add to 'transition' dict
			for (k,v) in attributes.items():
				if k == 'on' :
					self.transition['on'] = v
				elif k == 'to':
					self.transition['to'] = v
			self.transitions.append(self.transition)
			self.transition = {}
		elif name == 'if':
			# add two transition for 'then' and 'else'
			for (k,v) in attributes.items():
				if k == 'then' :
					self.transition['on'] = 'yes'
					self.transition['to'] = v
					self.transitions.append(self.transition)
					self.transition = {}
				elif k == 'else' :
					self.transition['on'] = 'no'
					self.transition['to'] = v
					self.transitions.append(self.transition)
					self.transition = {}

	def endElement(self, name):
		if name == 'flow':
			writeEndState()
		elif name in ('action-state', 'view-state', 'decision-state', 'subflow-state', 'end-state'):
			if self.isFirstState == True:
				writeStartState(self.id)
				self.isFirstState = False
			writeState(name, self.id, self.transitions)
			self.transitions = []

# Method for converting Spring XML to DOT file
def convertSpringXmlFile(filename):
	writeGraphStart(filename)

	# write graph body
	parser = xml.sax.make_parser()
	parser.setContentHandler(SpringXmlHandler())
	parser.parse(open(filename,"r"))

	writeGraphEnd()


if __name__ == '__main__':
	# read arguments
	parser = argparse.ArgumentParser(description="Generates a DOT file from a Spring Web Flow XML file")
	parser.add_argument('-f', action='store', dest='filename', required=True, help='Spring Web Flow XML file')
	parser.add_argument('-v', action='version', version='%(prog)s ' + __version__)
	args = parser.parse_args()

	# convert file
	convertSpringXmlFile(args.filename);
