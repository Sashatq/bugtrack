class Objects:

    def __init__(self, pname=None, description=None):
        self.pname = pname
        self.description = description

    def __repr__(self):
        return "%s:%s" % (self.pname, self.description)
