class Pila:
    def __init__(self):
        self.elementos = []
    
    def esta_vacia(self):
        return self.elementos == []
    def push(self, item):
        self.elementos.append(item)
    def pop(self):
        return self.elementos.pop()
    def ver(self):
        return self.elementos[len(self.elementos)-1]
    def tamano(self):
        return len(self.elementos)

s = Pila()
print(s.esta_vacia())
s.push('DOG')
s.push('CAT')
print(s.ver())
print(s.tamano())
s.pop()
print(s.ver())
print(s.tamano())