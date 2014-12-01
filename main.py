#! /usr/bin/python
import os
def getPackageLine(path):
	with open(path) as infile:
	    for line in infile:
	        if "package" in line:
	        	return line.lstrip("package").strip().rstrip(";") + "." + os.path.basename(path).rstrip(".java;")


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
