#! /usr/bin/python
import os
import JavaClass

def is_interface(path):
    with open(path) as infile:
        for line in infile:
            if "public interface" in line:
                return True
            elif "{" in line:
                break

        return False

def get_package(path):
    with open(path) as infile:
        for line in infile:
            if "package" in line:
                return line.lstrip("package").strip().rstrip(";") + "." + os.path.basename(path).rstrip(".java;")

def get_import_files(path, meaningful_classes):
    resultList = []
    with open(path) as infile:
        for line in infile:
            if "import" in line:
                mLine = line.lstrip("import").strip().rstrip(";")

                if mLine in meaningful_classes:
                    # print " +----> " + mLine
                    resultList.append(mLine)

            elif "{" in line:
                break

        return resultList

def get_java_files(path):
    resultList = []
    for name in os.listdir(path):

        if name != "src" and "src" not in path:
            continue

        if os.path.isdir(path+"/"+name):
            for each in get_java_files(path+"/"+name):
                resultList.append(each)

        if ".java" in name:
            resultList.append(path+"/"+name)

    return resultList


path = ""
meaningful_classes = []
class_statistic = {}
javaFilePaths = get_java_files(path)
for line in javaFilePaths:
    pLine = get_package(line)
    meaningful_classes.append(pLine)
    class_statistic[pLine] = 0

print "\n=== Statistics Details ===\n"
for line in javaFilePaths:

    jc = JavaClass.JavaClass(line)

    print '\-> ' + jc.path

    if is_interface(jc.path):
        print '(Interface) ' + jc.path
        continue
    else:
        print '\-> ' + jc.path

    for import_file in get_import_files(jc.path, meaningful_classes):
        class_statistic[import_file] = class_statistic[import_file] + 1
        print " +----> " + import_file

    print ''

mostly_called_class_name = ''
mostly_called_class_count = 0
for key in meaningful_classes:
    if class_statistic[key] > 0:
        print key + ": " + str(class_statistic[key])


    if class_statistic[key] > mostly_called_class_count:
        mostly_called_class_count = class_statistic[key]
        mostly_called_class_name = key

print "\n=== Statistics Summary ===\n"
print "mostly_called_class_name: " + mostly_called_class_name
print "mostly_called_class_count: " + str(mostly_called_class_count)
