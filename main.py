#! /usr/bin/python
import os

def isInterface(path):
	with open(path) as infile:
	    for line in infile:
	        if "public interface" in line:
	        	return True
	        elif "{" in line:
	        	break

	    return False

def getPackageLine(path):
	with open(path) as infile:
	    for line in infile:
	        if "package" in line:
	        	return line.lstrip("package").strip().rstrip(";") + "." + os.path.basename(path).rstrip(".java;")

def getImportLines(path):
	resultList = []
	with open(path) as infile:
	    for line in infile:
	        if "import" in line:
	        	mLine = line.lstrip("import").strip().rstrip(";")
	        	
	        	if mLine in x:
	        		# print " +----> " + mLine
	        		resultList.append(mLine)
	        		
	        elif "{" in line:
	        	break

	    return resultList

def getAllJavaFiles(path):
	resultList = []
	for name in os.listdir(path):

		if name != "src" and "src" not in path:
			continue

		if os.path.isdir(path+"/"+name):
			for each in getAllJavaFiles(path+"/"+name):
				resultList.append(each)

		if ".java" in name:
			resultList.append(path+"/"+name)

	return resultList


path = ""
global x
x = []
javaFilePaths = getAllJavaFiles(path)
for line in javaFilePaths:
	x.append(getPackageLine(line))

for line in javaFilePaths:
	print '\-> ' + line
	getImportLines(line)