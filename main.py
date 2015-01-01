#! /usr/bin/python
import os
import JavaClass


def get_package(path):
    with open(path) as infile:
        for line in infile:
            if "package" in line:
                return line.lstrip("package").strip().rstrip(";") + "." + os.path.basename(path).rstrip(".java;")


def get_java_files(path):
    resultList = []
    for name in os.listdir(path):

        if name != "src" and "src" not in path:
            continue

        if os.path.isdir(path + "/" + name):
            for each in get_java_files(path + "/" + name):
                resultList.append(each)

        if ".java" in name:
            resultList.append(path + "/" + name)

    return resultList


path = ""

meaningful_classes = []
class_statistic = {}
java_file_paths = get_java_files(path)
for line in java_file_paths:
    pLine = get_package(line)
    meaningful_classes.append(pLine)
    class_statistic[pLine] = 0

print "\n=== Statistics Details ===\n"
for line in java_file_paths:
    # print '\-> ' + line

    j = JavaClass.JavaClass(line, meaningful_classes)

    j.print_class()

    for subline in j.import_files:
        class_statistic[subline] = class_statistic[subline] + 1

mostly_called_class_name = ''
mostly_called_class_count = 0
max_length = len(str(max(class_statistic.values())))
for key in meaningful_classes:

    stat = class_statistic[key]
    if stat > 0:
        extra_spaces = " " * (max_length - len(str(stat)))
        print "[" + extra_spaces + str(stat) + "]: " + key

    if class_statistic[key] > mostly_called_class_count:
        mostly_called_class_count = class_statistic[key]
        mostly_called_class_name = key

print "\n=== Statistics Summary ===\n"
print "mostly_called_class_name: " + mostly_called_class_name
print "mostly_called_class_count: " + str(mostly_called_class_count)
