from colorama import Fore, Style

first_name = "AdA"
last_name = "LoVeLAce"

# Convertir a minúsculas (sin color)
print(first_name.lower(), last_name.lower())

# Convertir a formato título con color naranja (amarillo en terminal)
print(Fore.YELLOW + first_name.capitalize(), last_name.capitalize() + Style.RESET_ALL)

# Convertir a mayúsculas con color azul
print(Fore.BLUE + first_name.upper(), last_name.upper() + Style.RESET_ALL)

# Otra vez en minúsculas (sin color)
print(first_name.lower(), last_name.lower())
