# Manuel Pastrana Blazquez 

from componente_lexico import ComponenteLexico

class Lexico:
    def __init__(self, programa):
        '''
        Inicializa el analizador léxico con el programa a analizar y
        variables para rastrear la posición actual y el número de líneas.
        '''
        self.posicion = 0
        self.lineas = 1
        self.palabras_reservadas = {
            "break": "break",
            "do": "do",
            "else": "else",
            "float": "float",
            "for": "for",
            "if": "if",
            "int": "int",
            "while": "while"
        }
        # Añadimos el carácter # al final del programa para indicar su final.
        self.programa = programa + "#"

    def extrae_caracter(self):
        '''
        Avanza un carácter en el programa y lo devuelve.
        '''
        caracter = self.programa[self.posicion]
        self.posicion += 1
        return caracter

    def devuelve_caracter(self):
        '''
        Retrocede un carácter en el programa.
        '''
        self.posicion -= 1

    def get_componente_lexico(self):
        '''
        Realiza el análisis léxico del programa, descartando espacios y saltos de línea.
        Reconoce identificadores, palabras reservadas, números, operadores y delimitadores.
        '''
        while True:
            self.caracter = self.extrae_caracter()

            # Ignoramos espacios y saltos de línea, y contamos líneas al encontrar '\n'
            if self.caracter in [' ', '\r', '\n' ,'\t']:
                if self.caracter == '\n':
                    self.lineas += 1
                continue

            # Detecta el final del programa
            if self.caracter == '#':
                return ComponenteLexico("end_program")

            # Si no es espacio o salto de línea, seguimos con el análisis
            else:
                break

        # Identificación de palabras reservadas o identificadores
        if self.caracter.isalpha():
            lexema = self.caracter
            self.caracter = self.extrae_caracter()
            while self.caracter.isalnum():
                lexema += self.caracter
                self.caracter = self.extrae_caracter()
            self.devuelve_caracter()

            if lexema in self.palabras_reservadas:
                return ComponenteLexico(self.palabras_reservadas[lexema])  # Palabra reservada
            else:
                return ComponenteLexico("id", lexema)  # Identificador

        # Reconocimiento de números enteros o reales
        elif self.caracter.isdigit():
            numero = ""
            while self.caracter.isdigit():
                numero += self.caracter
                self.caracter = self.extrae_caracter()

            if self.caracter == '.':  # Número flotante
                numero += self.caracter
                self.caracter = self.extrae_caracter()
                while self.caracter.isdigit():
                    numero += self.caracter
                    self.caracter = self.extrae_caracter()
                self.devuelve_caracter()
                return ComponenteLexico("float", numero)
            else:  # Número entero
                self.devuelve_caracter()
                return ComponenteLexico("int", numero)

        # Reconocimiento de operadores y delimitadores
        else:
            operadores = {
                "=": "assignment", "==": "equals", "!=": "not_equals",
                "<": "less_than", "<=": "less_equals", ">": "greater_than", ">=": "greater_equals",
                "+": "add", "-": "subtract", "*": "multiply", "/": "divide", "%": "remainder",
                "&&": "and", "||": "or", "&": "bitwise_and", "|": "bitwise_or", "!": "not",
                ";": "semicolon", "(": "open_parenthesis", ")": "closed_parenthesis",
                "[": "open_square_bracket", "]": "closed_square_bracket",
                "{": "open_bracket", "}": "closed_bracket"
            }
            siguiente = self.extrae_caracter()
            token = self.caracter + siguiente

            if token in operadores:
                return ComponenteLexico(operadores[token])
            elif self.caracter in operadores:
                self.devuelve_caracter()
                return ComponenteLexico(operadores[self.caracter])
            else:
                raise ValueError(f"Caracter no reconocido: {self.caracter}")