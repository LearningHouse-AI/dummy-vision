class dog:
    attribute = "mamalia"

    def __init__(self, name):
        self.name = name

    def write(self):
        print("My name is {}".format(self.name))

rodger = dog("rodger")
tommy = dog("tommy")

# print("rodger is a {}".format(rodger.__class__.attribute))
# print("rodger is a {}".format(tommy.__class__.attribute))

rodger.write()
tommy.write()
