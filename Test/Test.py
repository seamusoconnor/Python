class holder(object):

    def __init__(self):
        self.value = 1000


    def adder(self, value):
        # type: (object) -> object
        self.value = value + 1
        return self.value

    def subber(self, value):
        self.value = value - 1
        return self.value

    def sq(self, value):
        self.value = self.value * self.value
        return self.value

    def destroy(self, value):
        self.value = 0
        return self.value



class calc(object):

    def plusser(self, value):
        self.value = value+value
        return self.value

