# Ahorcado
Este es un juego de adivinanza de palabras, donde se debe adivinar la palabra oculta ingresando letras de la misma antes que el contador llegue a 0. Si se ingresan letras que no pertenecen a la palabra oculta, el contador disminuye en 1.

El programa está escrito en Python usando la biblioteca Tkinter para la interfaz gráfica.

Funciones
select_país()
Función que selecciona una palabra aleatoria de una lista de países. Crea una tabla en la base de datos y agrega la palabra seleccionada en dicha tabla. Retorna la palabra con cada letra reemplazada por guiones.

cambio_letras()
Función que recibe una cadena de texto y devuelve cada carácter de la cadena como guiones bajos. Crea una tabla en la base de datos y agrega la cadena de guiones en dicha tabla.

comprobar_letras(letra)
Función que recibe una letra ingresada por el usuario y comprueba si la letra se encuentra en la palabra oculta. Si la letra está en la palabra, se reemplazan los guiones por la letra en la posición correspondiente. Si la letra no está en la palabra, se disminuye el contador en 1.

recupero_datos()
Función que recupera el contador y la palabra oculta de la base de datos.

final()
Función que muestra un mensaje de finalización del juego y pregunta si desea jugar de nuevo o salir.

Clase Ahorcado
init(self)
Constructor de la clase que inicializa la ventana de bienvenida.

cambio_ventana(self, *event)
Método que crea la ventana de juego cuando se presiona el botón 'Entrar'. Oculta la ventana de bienvenida.

ventana_juego(self)
Método que crea la ventana de juego.

llamadas(self, *event)
Método que llama a las funciones comprobar_letras() y recupero_datos(), actualiza la interfaz gráfica y muestra la palabra oculta con las letras adivinadas.

Uso
Ejecutar el archivo ahorcado.py para iniciar el juego. Se muestra una ventana de bienvenida donde se debe ingresar el nombre del jugador. Luego se abre la ventana de juego y se puede comenzar a adivinar la palabra ingresando letras en el cuadro de texto y presionando el botón 'Comprobar' o la tecla 'Enter'.

El programa almacena los datos de la partida en una base de datos SQLite y permite jugar tantas veces como se desee. Si se desea salir del programa, se debe presionar el botón de la 'X' en la ventana de juego.
