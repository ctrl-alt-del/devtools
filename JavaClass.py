class JavaClass(object):
    def __init__(self, path):
        self.path = path

    def print_class(self):
        if self.is_interface:
            print '(Interface) ' + self.path
            return
        else:
            print '\-> ' + self.path

        for subline in self.import_files:
            print " +----> " + subline

        print ''