#! /usr/bin/python
import os

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
    print '\-> ' + line
    if is_interface(line):
        print '(Interface) ' + line
        continue
    else:
        print '\-> ' + line

    for subline in get_import_files(line, meaningful_classes):
        class_statistic[subline] = class_statistic[subline] + 1
        print " +----> " + subline

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
