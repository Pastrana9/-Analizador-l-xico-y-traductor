# Manuel Pastrana Blazquez 

from lexico import Lexico

def main():
    # Programa de prueba para el analizador léxico
    programa = '''float suma = 0.0;\nint [10] v;\nfor (int k=0; k<10; k=k+1) {\nif (k % 2 == 0)\nsuma = suma + k*10.5;\nelse\nsuma = suma + k*15.75;\nv[i] = suma;\n}\nif (suma <= 25.0)\nsuma = suma / 2.5;\nelse\nsuma = suma * 4.5;'''

    # Instanciamos el analizador léxico con el programa
    lexico = Lexico(programa)

    print(f"Programa de prueba:\n{programa}\n")

    # Contador de componentes léxicos
    c = 0

    # Bucle principal para obtener cada componente léxico
    while True:
        etiqueta_lexica = lexico.get_componente_lexico()
        print(etiqueta_lexica)
        if etiqueta_lexica.get_etiqueta() == "end_program":
            break
        c += 1

if __name__ == "__main__":
    main()
