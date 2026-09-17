# Backend Python API

API REST creada con **Flask** para administrar jugadores almacenados en la tabla `jugadores` de Supabase.

## Estado actual

La aplicación, definida en `main.py`, permite:

- Consultar todos los jugadores.
- Crear jugadores con nombre y estilo.
- Consultar un jugador por su identificador.
- Eliminar un jugador por su identificador.

## Requisitos

- Python 3
- Flask
- Una conexión de Supabase configurada en `db.py`.

## Ejecutar el proyecto

Desde la carpeta raíz del repositorio, ejecuta:

```bash
python -m flask --app main run --debug
```

La API quedará disponible normalmente en `http://127.0.0.1:5000`.

## Endpoints disponibles

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/api/jugadores` | Devuelve todos los jugadores. |
| `POST` | `/api/jugadores` | Crea un jugador. |
| `GET` | `/api/jugadores/<id>` | Devuelve el jugador cuyo identificador coincide con `id`. |
| `DELETE` | `/api/jugadores/<id>` | Elimina el jugador cuyo identificador coincide con `id`. |

### Crear un jugador

La solicitud debe enviarse en formato JSON. El campo `nombre` es obligatorio y `estilo` es opcional.

```json
{
  "nombre": "Cesar",
  "estilo": "Ofensivo"
}
```

Si no se proporciona `nombre`, la API responde con `400`:

```json
{
  "error": "El campo 'nombre' es requerido"
}
```

### Respuestas cuando no existe el jugador

Las rutas de consulta y eliminación responden con `404` cuando el identificador no existe:

```json
{
  "error": "Jugador no encontrado"
}
```

### Ejemplos

```text
GET /api/jugadores
POST /api/jugadores
GET /api/jugadores/1
DELETE /api/jugadores/1
```
