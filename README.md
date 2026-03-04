# Ahorcado-AARON-VELOZ

FECHA: 03/03/2026

Datos:

Estudiante: Aarón Veloz

Asignatura: LOGICA DE PROGRAMACION

Proyecto: Juego del Ahorcado en Python


OBJETIVO DEL PROGRAMA

El objetivo de este proyecto es desarrollar una versión del juego clásico Ahorcado utilizando el lenguaje de programación Python.
El programa permite que el jugador adivine una palabra secreta letra por letra, teniendo un número limitado de intentos.

Durante el juego, el sistema muestra el estado actual de la palabra, las letras incorrectas utilizadas y el número de intentos restantes.
El juego finaliza cuando el jugador logra adivinar la palabra completa o cuando se queda sin intentos disponibles.

Este proyecto permite aplicar conceptos fundamentales de programación como estructuras de datos, funciones, ciclos y condicionales.

Explicación de las principales funcionalidades del código

El programa está organizado en diferentes funciones que permiten controlar el funcionamiento del juego.

Selección de palabra aleatoria

El programa utiliza un diccionario de categorías y palabras, desde el cual selecciona una palabra al azar al inicio de cada partida. Esto permite que cada juego sea diferente.

Inicialización del juego

Cuando comienza una nueva partida, el programa inicializa las variables necesarias como:

-la palabra oculta

-las letras adivinadas

-las letras incorrectas

-los intentos restantes

Estas variables permiten controlar el estado del juego.

Interfaz del juego

Durante cada turno, el programa muestra en pantalla:

-el dibujo del ahorcado según los intentos restantes

-la palabra oculta

-las letras incorrectas

-el número de intentos disponibles

Esto permite al jugador visualizar su progreso durante el juego.

Procesamiento de letras

El jugador ingresa una letra en cada turno.
El programa valida que la letra sea correcta y luego verifica si pertenece a la palabra.

Si la letra está en la palabra, se actualiza la palabra oculta.

Si la letra no está, se reduce el número de intentos.

Verificación de victoria o derrota

Después de cada intento el programa verifica dos condiciones:

-Si el jugador ha completado la palabra (victoria).

-Si el jugador se quedó sin intentos (derrota).

En ambos casos el programa muestra el resultado de la partida.

Repetición del juego

Al finalizar una ronda, el programa pregunta al jugador si desea jugar nuevamente.
Si el usuario responde afirmativamente, el juego se reinicia con una nueva palabra.

Estructuras utilizadas en el programa

El código utiliza diferentes estructuras de programación:

Variables para almacenar información del juego.

Listas para guardar letras adivinadas y letras incorrectas.

Diccionarios para organizar las palabras por categorías.

Tuplas para devolver múltiples valores desde funciones.

Funciones para organizar el código y dividir el programa en tareas específicas.

Condicionales para tomar decisiones durante el juego.

Ciclos para repetir el proceso del juego mientras esté activo.


