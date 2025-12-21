import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))
    
    def serialize(self, filename):
        with open(filename, 'wb') as afile:
            pickle.dump(self, afile)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as afile:
                return pickle.load(afile)
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            return
