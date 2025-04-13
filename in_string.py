def check_vowels():
    nombre= input("Ingresar nombre: ")
    vocales="aeiou"
    for vocal in vocales:
        contiene= vocal in nombre.lower()
        print(f"contiene {vocal}: {Contiene}")
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
