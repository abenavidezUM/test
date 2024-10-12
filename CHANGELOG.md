# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.7.0] - 2024-09-08
### Modificando
- **game/board.py**:
  - Se ha implementado la documentacion el codigo en 'Docstrings'.
- **game/interfaz.py**: 
  - Se ha implementado la documentacion el codigo en 'Docstrings'.
  - Se ha modificado el metodo `draw` para que la clase `Interfaz` no cambie el turno de la clase `Chess`.
- **game/chess_game.py**:
  - Se ha implementado la documentacion el codigo en 'Docstrings'.
  - Se ha agregado el método `next_turn` para saber de quien es el siguiente turno.
  - Se ha agregado el método `check_move` para que la verificación del movimiento y del estado no sea dentro del metodo `move`.
- **tests/test_chess_game.py**:
  - Se ha agregado el test para el metodo `next_turn`.
## [0.6.7] - 2024-09-05
### Modificando
- **game/interfaz.py**:
  - Se ha modificado el codigo para cuando termine el juego, vuelva a mostrar el menu principal.
## [0.6.6] - 2024-09-03
### Modificando
- **game/board.py**:
  - Se ha modificado la forma de establecer una pieza al moverla en el tablero.
## [0.6.5] - 2024-08-30
### Modificando
- **tests/test_interfaz.py**:
  - Se han agregado las ultimas pruebas para la clase `Interfaz`.
- **game/board.py**:
  - Se ha agregado la excepción `CantEatKingError` para que no pueda comer al rey de tu oponente.
- **game/exceptions.py**:
  - Se ha agregado la excepción `CantEatKingError` para que no pueda comer al rey de tu oponente.
## [0.6.0] - 2024-08-29
### Modificando
- **game/chess_game.py**:
  - Se ha refactorizado el codigo para tener inputs mas legibles. 
- **game/interfaz.py**:
  - Se ha arreglado el codigo para cerrar el bucle y terminar el juego.
- **tests/test_interfaz.py**:
  - Se han agregado nuevas pruebas para la clase `Interfaz`.
## [0.5.2] - 2024-08-28
### Modificando
- **tests/test_interfaz.py**:
  - Se han agregado nuevas pruebas para la clase `Interfaz`.
- **game/interfaz.py**:
  - Se ha refactorizado el codigo para evitar issues de codeclimate.
## [0.5.1] - 2024-08-27
## Modificando
- **game/pieces**:
  - Modificacion en `GENERAL` de todas la piezas.
  - Se han refactorizado las piezas para obviar la creacion de atributos de clase y heredarlos directamente de `Piece`.
## [0.5.0] - 2024-08-26
## Modificando
- **game/pieces**:
  - Modificacion en `GENERAL` de todas la piezas.
  - Se han refactorizado las piezas para solucionar problemas de codeclimate "bloques identicos".
- **game/pieces/piece.py**:
  - Se ha implementado método `get_coordinates` para obtener las coordenadas de la piez y mejorar movimientos.
  - Se ha implementado método `diagonal_moves` para obtener las posiciones posibles de los movimientos diagonales, para `queen` y `bishop`.
  - Se ha implementado método `horizontal_moves` para obtener las posiciones posibles de los movimientos horizontales, para `queen` y `rook`.
  - Se ha implementado método `vertical_moves` para obtener las posiciones posibles de los movimientos verticales, para `queen` y `rook`.
- **game/pieces/pawn.py**:
  - Se ha refactorizado `check_move`, dividiendolo asi en métodos `is_valid_white_move`, `is_valid_black_move`, `is_valid_pawn_move`y `move_one_cell`, para mejorar el código y evitar issues de codeclimate.
- **tests/test_interfaz.py**:
  - Se han agregado algunas pruebas para la clase `Interfaz`.
## [0.4.5] - 2024-08-25
### Modificando
- **game/exceptions.py**:
  - Se han refactorizado los mensajes de excepciones para arreglar issues de codeclimate.
- **game/interfaz.py**:
  - Se ha refactorizado del codigo para que sea más legible y fácil de entender, implementado así método como:
    - `handle_resignation` para que el jugador resista la ventaja.
    - `handle_draw` para que el jugador rechace el empate.
    - `draw` para que el jugador decide si acepta o rechaza el empate.
    - `turn_menu` para que el jugador decida si quiere continuar o no.
    - `display_board_and_turn` para mostrar el tablero y el turno.
    - `get_move_input` para que el jugador ingrese su movimiento.
    - `attempt_move` para que el jugador intente mover la pieza.
  - Se ha implementado método `clear_terminal` para limpiar la terminal y hacer mas amigable la interfaz.
## [0.4.0] - 2024-08-23
### Modificando
- **game/board.py**:
  - Método `check_victory` para saber cuales piezas quedan en el tablero.
- **game/chess_game.py**:
  - Método `check_victory` para verificar el estado del juego.
## [0.3.0] - 2024-08-22
### Agregando
- **tests/test_interfaz.py**:
  - Añadidos tests para la clase `Interfaz`, aún sigue en proceso.
- **tests/test_bishop.py**:
  - Añadidos tests para la clase `Bishop`.
- **tests/test_king.py**:
  - Añadidos tests para la clase `King`.
- **tests/test_knight.py**:
  - Añadidos tests para la clase `Knight`.
- **tests/test_pawn.py**:
  - Añadidos tests para la clase `Pawn`.
- **tests/test_piece.py**:
  - Añadidos tests para la clase `Piece`.
- **tests/test_queen.py**:
  - Añadidos tests para la clase `Queen`.
- **tests/test_rook.py**:
  - Añadidos tests para la clase `Rook`.
### Modificando
- **game/chess_game.py**:
  - Método `validate_cords` para validar las coordenadas de las piezas.
  - Método `print_board` para imprimir el tablero de ajedrez.
  - Método `own_pieces` para obtener la pieza que posee el usuario.
- **game/board.py**:
  - Método `color_pieces` para obtener el color de la pieza en una posición.
- **pieces/**: Implementado método para validar si un movimiento es válido.
  - Método `check_move` en cada clase de pieza para validar si un movimiento es válido.
- **game/exceptions.py**: Implementando nuevas excepciones.
  - Excepción `InvalidPieceMovement` para errores de movimientos de piezas.
  - Excepción `ColorError` para errores de piezas de color diferente.
## [0.2.0] - 2024-08-15
### Agregando
- **chess_game.py**:
  - Método `move` para mover piezas en el tablero, con validación de coordenadas.
  - Método `change_turn` para alternar entre los turnos de los jugadores (blanco y negro).
- **exceptions.py**: Implementado excepciones para los errores que pueden ocurrir en el juego.
- **test_chess.py**: Implementado test unitarios para  la clase `Chess`.
- **test_board.py**: Implementado test unitarios la clase `Board`.
### Modificando
- **pieces/**: Implementado los metodos para mover las piezas.
  - Método `get_position` en cada clase de pieza para obtener la posición de la pieza.
  - Método `set_position` en cada clase de pieza para establecer la posición de la pieza.
- **cli.py** -> **interfaz.py**: Renombrado del archivo `cli.py` a `interfaz.py` y reformado para implementar la clase `Interfaz` que gestiona la interacción del usuario con el juego.
  - Método `menu` para mostrar la interfaz de línea de comandos.
  - Método `validate_option` para validar las opciones del menú.
  - Método `start_game` para iniciar el juego.
- **board.py**: Modificado tablero inicial para el juego.
  - Metodo `find_piece` que busca la posición de una pieza en el tablero.
  - Método `move` para mover piezas en el tablero, con validación de coordenadas.
  - Método `validate_move` para validar si un movimiento es válido.
  - Método `execute_move` para ejecutar el movimiento en el tablero.
- **main.py**: Implementado archivo principal para ejecutar el juego.
- **.coveragerc**: Modificado para correr los test unitarios.
## [0.1.0] - 2024-08-13
### Agregando
- **chess.py**: Implementada la clase `Chess` que gestiona el tablero y el turno de los jugadores.
  - Método `move` para mover piezas en el tablero, con validación de coordenadas.
  - Método `change_turn` para alternar entre los turnos de los jugadores (blanco y negro).
- **cli.py**: Creada una interfaz de línea de comandos (CLI) básica para interactuar con el juego de ajedrez.
  - Función `main` que inicializa el juego.
  - Función `play` que gestiona la interacción del usuario para mover piezas en el tablero.
- **board.py**: Creado un tablero inicial para el juego.
  - Método `get_piece` que obtiene la pieza que se encuentra en x posicion.
- **Dockerfile**: Para crear un entorno contenedor para ejecutar el proyecto en Python.
## [0.0.1] - 2024-08-08
### Agregando
- Integracion con CircleCI.
- Intregración con CodeClimate.
- Archivo README con información básica.
- Archivo CHANGELOG para registrar cambios.
- Archivo main.py con función working() para probar la funcionalidad.
- Archivo test_example.py con test unitarios para probar la funcionalidad.
