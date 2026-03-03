"""
JUEGO DEL AHORCADO - VERSIÓN COMPLETA
Programa que implementa el juego del ahorcado usando:
- Variables, Condicionales, Ciclos, Listas, Diccionarios, Tuplas y Funciones
"""

import random

# ============================================================================
# VARIABLES GLOBALES Y CONSTANTES
# ============================================================================
DIBUJOS_AHORCADO = (
    """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    --------
    """
)

# DICCIONARIO CON CATEGORÍAS Y PALABRAS
PALABRAS_AHORCADO = {
    "animales": ["gato", "perro", "elefante", "jirafa", "cocodrilo", "mariposa", "aguila"],
    "ciudades": ["madrid", "barcelona", "buenos aires", "nueva york", "tokio", "paris", "roma"],
    "deportes": ["futbol", "basquetbol", "tenis", "voleibol", "natacion", "ciclismo"],
    "colores": ["rojo", "azul", "verde", "amarillo", "purpura", "naranja", "rosa"],
    "frutas": ["manzana", "platano", "naranja", "fresa", "piña", "sandía", "melocoton"]
}

# ============================================================================
# FUNCIONES DEL JUEGO
# ============================================================================

def obtener_palabra_aleatoria(diccionario_palabras):
    """
    Selecciona una categoría aleatoria y devuelve una palabra.
    Retorna una tupla: (palabra, categoría)
    """
    categorias = list(diccionario_palabras.keys())
    categoria_elegida = random.choice(categorias)
    palabra = random.choice(diccionario_palabras[categoria_elegida])
    return (palabra.upper(), categoria_elegida)

def inicializar_juego(palabra):
    """
    Inicializa las variables del juego.
    Retorna un diccionario con el estado del juego.
    """
    estado_juego = {
        "palabra_oculta": ["_" for _ in palabra],
        "letras_adivinadas": [],
        "letras_incorrectas": [],
        "intentos_restantes": 6,
        "juego_activo": True
    }
    return estado_juego

def mostrar_interfaz(palabra_oculta, letras_incorrectas, intentos_restantes):
    """
    Muestra la interfaz del juego con el estado actual.
    """
    print("\n" + "="*50)
    print(DIBUJOS_AHORCADO[6 - intentos_restantes])
    print("Palabra: " + " ".join(palabra_oculta))
    print(f"Intentos restantes: {intentos_restantes}")
    print(f"Letras incorrectas: {', '.join(letras_incorrectas) if letras_incorrectas else 'Ninguna'}")
    print("="*50)

def obtener_letra_valida(letras_adivinadas):
    """
    Solicita una letra al jugador y valida que sea válida.
    Devuelve una letra válida.
    """
    while True:
        letra = input("\nIngresa una letra: ").upper()
        
        # CONDICIONALES: Validar entrada
        if len(letra) != 1:
            print("❌ Debes ingresar solo UNA letra.")
            continue
        
        if not letra.isalpha():
            print("❌ Debes ingresar una letra válida.")
            continue
        
        if letra in letras_adivinadas:
            print(f"❌ Ya habías adivinado la letra {letra}.")
            continue
        
        return letra

def procesar_letra(letra, palabra, estado_juego):
    """
    Procesa la letra ingresada y actualiza el estado del juego.
    """
    estado_juego["letras_adivinadas"].append(letra)
    
    # CONDICIONAL: Verificar si la letra está en la palabra
    if letra in palabra:
        # Actualizar la palabra oculta
        for i, char in enumerate(palabra):
            if char == letra:
                estado_juego["palabra_oculta"][i] = letra
        print(f"✓ ¡Correcto! La letra {letra} está en la palabra.")
    else:
        estado_juego["letras_incorrectas"].append(letra)
        estado_juego["intentos_restantes"] -= 1
        print(f"✗ La letra {letra} NO está en la palabra.")

def verificar_victoria(palabra_oculta, palabra):
    """
    Verifica si el jugador ha ganado.
    """
    return "_" not in palabra_oculta

def verificar_derrota(intentos_restantes):
    """
    Verifica si el jugador ha perdido.
    """
    return intentos_restantes <= 0

def mostrar_estadisticas(intentos_usados, letras_correctas, letras_incorrectas):
    """
    Muestra estadísticas del juego.
    Recibe tuplas con información del juego.
    """
    print("\n" + "="*50)
    print("ESTADÍSTICAS DEL JUEGO")
    print("="*50)
    print(f"Intentos usados: {intentos_usados}")
    print(f"Letras correctas: {len(letras_correctas)}")
    print(f"Letras incorrectas: {len(letras_incorrectas)}")
    print(f"Precisión: {(len(letras_correctas) / (len(letras_correctas) + len(letras_incorrectas)) * 100):.1f}%" 
          if (len(letras_correctas) + len(letras_incorrectas)) > 0 else "N/A")

def jugar_ahorcado():
    """
    Función principal que controla el flujo del juego.
    CICLO: while para jugar múltiples rondas
    """
    print("\n" + "="*50)
    print("🎮 BIENVENIDO AL JUEGO DEL AHORCADO 🎮")
    print("="*50)
    
    jugar_otra_ronda = True
    
    # CICLO PRINCIPAL: Permite jugar varias rondas
    while jugar_otra_ronda:
        # Obtener palabra aleatoria (TUPLA)
        palabra, categoria = obtener_palabra_aleatoria(PALABRAS_AHORCADO)
        print(f"\n📌 Categoría: {categoria.upper()}")
        
        # Inicializar juego (DICCIONARIO)
        estado = inicializar_juego(palabra)
        
        # CICLO: Mientras el juego esté activo
        while estado["juego_activo"]:
            mostrar_interfaz(estado["palabra_oculta"], 
                           estado["letras_incorrectas"], 
                           estado["intentos_restantes"])
            
            # Obtener letra del jugador
            letra = obtener_letra_valida(estado["letras_adivinadas"])
            
            # Procesar la letra
            procesar_letra(letra, palabra, estado)
            
            # CONDICIONALES: Verificar condiciones de fin de juego
            if verificar_victoria(estado["palabra_oculta"], palabra):
                estado["juego_activo"] = False
                print("\n" + "="*50)
                print("🎉 ¡¡¡GANASTE!!! 🎉")
                print(f"La palabra era: {palabra}")
                print("="*50)
                
                # Mostrar estadísticas (usando TUPLAS)
                intentos_usados = 6 - estado["intentos_restantes"]
                mostrar_estadisticas(
                    intentos_usados,
                    tuple(estado["letras_adivinadas"]),  # TUPLA: letras correctas
                    tuple(estado["letras_incorrectas"])   # TUPLA: letras incorrectas
                )
                
            elif verificar_derrota(estado["intentos_restantes"]):
                estado["juego_activo"] = False
                print("\n" + "="*50)
                print("💀 ¡¡¡GAME OVER!!! 💀")
                print(f"La palabra era: {palabra}")
                print("="*50)
                
                # Mostrar estadísticas
                intentos_usados = 6
                mostrar_estadisticas(
                    intentos_usados,
                    tuple(estado["letras_adivinadas"]),
                    tuple(estado["letras_incorrectas"])
                )
        
        # Preguntar si jugar otra ronda
        while True:
            respuesta = input("\n¿Deseas jugar otra ronda? (S/N): ").upper()
            if respuesta in ["S", "N"]:
                jugar_otra_ronda = (respuesta == "S")
                break
            print("❌ Por favor ingresa S o N.")
    
    print("\n" + "="*50)
    print("¡Gracias por jugar! 👋")
    print("="*50)

# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    jugar_ahorcado()
