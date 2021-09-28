from library import Base

class Derived(Base):
    def __init__(self, work):
        super().__init__()
        self.work = work
    def bar(self):
        return 'bar'