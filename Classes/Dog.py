class Dog:
    def __init__(self, name = '', color = ''):
        self._name = ''
        self._color = ''


    def setName(self, name):
        self._name = name

    def setColor(self, color):
        self._color = color


    def getName(self):
        return self._name
    
    def getColor(self):
        return self._color

