# Manuel Pastrana Blazquez 

from traductor_postfijo import TraductorExpresionPostfijo
from lexico import Lexico

def main():
    # Traducción
    expresion = "(25 * (2 + 2)) / 2 * 3"
    lexico = Lexico(expresion)
    expr = TraductorExpresionPostfijo(lexico)

    print(f"\nLa expresión: {expresion} en notación postfija es: {expr.postfijo()} "
          f"y su valor es: {expr.calculate()}")

    # Análisis Léxico
    programa = "(25*(2+2))/2*3"
    lexico = Lexico(programa)
    
    print(f"\nTest léxico básico\t{programa}\n")
    
    etiqueta_lexica = lexico.get_componente_lexico()
    while etiqueta_lexica.get_etiqueta() != "end_program":
        print(etiqueta_lexica)
        etiqueta_lexica = lexico.get_componente_lexico()

if __name__ == "__main__":
    main()

