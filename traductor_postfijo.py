# Manuel Pastrana Blazquez 

from componente_lexico import ComponenteLexico
from lexico import Lexico

class TraductorExpresionPostfijo:
    def __init__(self, lexico):
        self.lexico = lexico
        self.componente_lexico = self.lexico.get_componente_lexico()
        self.pila = []  # Pila donde se almacenarán los operadores y operandos en notación postfija
        self.postfijo_str = ""  # String final en notación postfija

    def postfijo(self):
        self.expresion()  # Inicia la traducción desde la producción principal
        self.postfijo_str = " ".join(self.pila)  # Devuelve el resultado en postfijo
        return str(self.postfijo_str)

    # Expresión → término más_terminos
    def expresion(self):
        self.termino()  # Procesamos el primer término
        self.mas_terminos()  # Procesamos posibles más términos (operaciones + o -)

    # Término → factor más_factores
    def termino(self):
        self.factor()  # Procesamos el factor (número o expresión entre paréntesis)
        self.mas_factores()  # Procesamos posibles más factores (operaciones * o /)

    # Factor → num | (expresión)
    def factor(self):
        if self.componente_lexico.get_etiqueta() in {"int", "float"}:
            # Añadimos el número directamente a la pila postfija
            self.pila.append(self.componente_lexico.get_valor())
            self.compara(self.componente_lexico.get_etiqueta())
        elif self.componente_lexico.get_etiqueta() == "open_parenthesis":
            # Procesamos la expresión dentro de los paréntesis
            self.compara("open_parenthesis")
            self.expresion()
            self.compara("closed_parenthesis")
        else:
            raise SyntaxError(f"ERROR: Se esperaba un número o un paréntesis abierto, pero se encontró {self.componente_lexico.get_etiqueta()}")

    # Más términos → + término más_terminos | - término más_terminos | epsilon
    def mas_terminos(self):
        if self.componente_lexico.get_etiqueta() == "add":
            self.compara("add")
            self.termino()
            self.pila.append("+")  # Añadimos el operador a la pila postfija
            self.mas_terminos()
        elif self.componente_lexico.get_etiqueta() == "subtract":
            self.compara("subtract")
            self.termino()
            self.pila.append("-")  # Añadimos el operador a la pila postfija
            self.mas_terminos()

    # Más factores → * factor más_factores | / factor más_factores | epsilon
    def mas_factores(self):
        if self.componente_lexico.get_etiqueta() == "multiply":
            self.compara("multiply")
            self.factor()
            self.pila.append("*")  # Añadimos el operador a la pila postfija
            self.mas_factores()
        elif self.componente_lexico.get_etiqueta() == "divide":
            self.compara("divide")
            self.factor()
            self.pila.append("/")  # Añadimos el operador a la pila postfija
            self.mas_factores()

    def compara(self, etiqueta_lexica):
        # Comparamos el componente léxico actual con el esperado y avanzamos
        if self.componente_lexico.get_etiqueta() == etiqueta_lexica:
            self.componente_lexico = self.lexico.get_componente_lexico()
        else:
            raise SyntaxError(f"ERROR: Se esperaba {etiqueta_lexica}")

    def calculate(self):
        # Evalúa la expresión postfija utilizando una pila
        pila_valor = []
        tokens = self.postfijo_str.strip().split()

        for token in tokens:
            if self.es_numerico(token):
                pila_valor.append(float(token))
            else:
                num2 = pila_valor.pop()
                num1 = pila_valor.pop()
                if token == "+":
                    pila_valor.append(num1 + num2)
                elif token == "-":
                    pila_valor.append(num1 - num2)
                elif token == "*":
                    pila_valor.append(num1 * num2)
                elif token == "/":
                    if num2 != 0:
                        pila_valor.append(num1 / num2)  # División flotante
                    else:
                        raise ZeroDivisionError("ERROR: División por cero.")
                else:
                    raise ValueError(f"ERROR: Operador desconocido {token}")

        return pila_valor.pop() if pila_valor else "La expresión está vacía"

    def es_numerico(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False
