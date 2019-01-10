class Objects:

    def __init__(self, pname=None, description=None):
        self.pname = pname
        self.description = description

    def __repr__(self):
        return "%s:%s" % (self.pname, self.description)

    def __eq__(self, other):
        return (self.pname is None or other.pname is None or self.pname == other.pname) \
               and self.description == other.description

