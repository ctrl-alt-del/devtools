class JavaClass(object):
    def __init__(self, path, meaningful_classes):
        self.path = path
        self.meaningful_classes = meaningful_classes
        self.is_interface = self.is_interface()
        self.import_files = self.get_import_files()
        self.num_of_import_files = len(self.import_files)

    def get_import_files(self):

        _import_files = []

        with open(self.path) as infile:
            for line in infile:
                if "import" in line:
                    mLine = line.lstrip("import").strip().rstrip(";")

                    if mLine in self.meaningful_classes:
                        _import_files.append(mLine)

                elif "{" in line:
                    break

        return _import_files

    def is_interface(self):
        with open(self.path) as infile:
            for line in infile:
                if "public interface" in line:
                    return True
                elif "{" in line:
                    break

        return False

    def print_class(self):
        if self.is_interface:
            print '(Interface) ' + self.path
            return
        else:
            print '\-> ' + self.path

        for subline in self.import_files:
            print " +----> " + subline

        print ''