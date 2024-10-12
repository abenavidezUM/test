# CHESS GAME
Proyecto creado por Agustin Correnti

## Cómo Instalar el Juego

El juego se ejecuta utilizando Docker. Sigue los siguientes pasos para instalar y correr el juego:

1. **Instalar Docker**  
   Si no tienes Docker instalado, ejecuta el siguiente comando:
```bash
    $ sudo apt install docker
```
2. **Crear la imagen de Docker del juego**  
   Para construir la imagen Docker del juego, ejecuta:
```bash
    $ sudo docker buildx build -t ajedrez-2024-aguscorren . --no-cache
```
3. **Ejecutar los tests e iniciar el juego**  
   Una vez creada la imagen, puedes ejecutar el siguiente comando para correr los tests e iniciar el juego:
```bash
    $ sudo docker run -i ajedrez-2024-aguscorren
```
## Reglas del Juego
El juego sigue las reglas básicas del ajedrez con algunas modificaciones:
- `Reglas originales del ajedrez`: Consultarlas [aquí](https://es.wikipedia.org/wiki/Leyes_del_ajedrez)
- `Reglas de este juego`: En este ajedrez se respetan los movimientos de las piezas como en el ajedrez tradicional. Sin embargo, no se implementan reglas como jaque, jaque mate, ni movimientos especiales.
## Cómo Jugar
- El juego se basa en turnos alternos, donde cada jugador mueve una pieza según las reglas del ajedrez tradicional. A continuación se describe la interfaz del juego:

- La interfaz ofrece un menú con las opciones de `Move piece`, `Draw` y `Resign`.
    - `Move piece`: 
    Permite mover una pieza. Se solicita la posición actual de la pieza y la posición a la que se desea mover, ambas utilizando notación algebraica (Ej: A1, B3).
        - Si el movimiento es válido, se efectúa; si no, se cancela y vuelve a pedirle al jugador que haga el movimiento. Después, se verifica si un jugador ha ganado.
    - `Draw`: Permite ofrecer tablas (empate). Si el oponente acepta, el juego termina en empate. Si no, el jugador que ofreció las tablas vuelve a su turno.
    - `Resign`: Permite rendirse, lo que otorga la victoria al oponente.

## Cómo Ganar
Para ganar, tu oponente debe quedar solo con el Rey, mientras que tú con el Rey y al menos una pieza adicional. Es decir, que el primero que se quede sin piezas (exceptuando al Rey), pierde.
# Integraciones 
## CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-AgusCorren/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-AgusCorren/tree/main)
## Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/d8f649c936fdc917525f/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-AgusCorren/maintainability)
## Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/d8f649c936fdc917525f/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-AgusCorren/test_coverage)