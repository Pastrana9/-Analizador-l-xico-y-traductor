# Manuel Pastrana Blazquez

class ComponenteLexico:
    '''
    Clase que representa un componente léxico con una etiqueta y un valor opcional.
    La etiqueta indica el tipo de token (e.g., 'int', 'add', 'id'), y el valor es el lexema (si corresponde).
    '''
    def __init__(self, etiqueta, valor=None):
        self.etiqueta = etiqueta
        self.valor = valor

    def get_etiqueta(self):
        return self.etiqueta

    def get_valor(self):
        return self.valor

    def __str__(self):
        # Si el componente tiene un valor (lexema), lo incluimos en la representación
        if self.valor:
            return f"<{self.etiqueta}, {self.valor}>"
        return f"<{self.etiqueta}>"
