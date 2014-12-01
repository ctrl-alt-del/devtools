#! /usr/bin/python
import os

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
