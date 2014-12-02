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
class_statistic = {}
javaFilePaths = getAllJavaFiles(path)
for line in javaFilePaths:
	pLine = getPackageLine(line)
	x.append(pLine)
	class_statistic[pLine] = 0

print "\n=== Statistics Details ===\n"
for line in javaFilePaths:
	print '\-> ' + line
	if isInterface(line):
		print '(Interface) ' + line
		continue
	else:
		print '\-> ' + line

	for subline in getImportLines(line):
		class_statistic[subline] = class_statistic[subline] + 1
		print " +----> " + subline

	print ''

mostly_called_class_name = ''
mostly_called_class_count = 0
for key in x:	if class_statistic[key] > mostly_called_class_count:
	if class_statistic[key] > mostly_called_class_count:
		mostly_called_class_count = class_statistic[key]
		mostly_called_class_name = key

print "\n=== Statistics Summary ===\n"
print "mostly_called_class_name: " + mostly_called_class_name
print "mostly_called_class_count: " + str(mostly_called_class_count)
