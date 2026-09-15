# Backend Python API

API REST inicial creada con **Flask** para consultar una lista de usuarios almacenada temporalmente en memoria.

## Estado actual

Hasta ahora el proyecto cuenta con:

- Una aplicación Flask definida en `main.py`.
- Una colección inicial de cuatro usuarios (`id` y `nombre`).
- Endpoints de solo lectura para consultar todos los usuarios, uno por identificador y uno por nombre.
- Un `.gitignore` que evita incluir el archivo `.env` en el repositorio.

Los datos aún no se guardan en una base de datos: se reinician cada vez que se detiene y vuelve a iniciar la aplicación.

## Requisitos

- Python 3
- Flask

Instala Flask con:

```bash
pip install flask
```

## Ejecutar el proyecto

Desde la carpeta raíz del repositorio, ejecuta:

```bash
python -m flask --app main run --debug
```

La API quedará disponible normalmente en `http://127.0.0.1:5000`.

## Endpoints disponibles

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/api/usuarios` | Devuelve todos los usuarios. |
| `GET` | `/api/usuarios/<id>` | Devuelve el usuario cuyo identificador coincide con `id`. |
| `GET` | `/api/usuarios/<nombre>` | Devuelve el usuario cuyo nombre coincide con `nombre`. |

Cuando no se encuentra un usuario por identificador o por nombre, la API responde con el código `404` y el siguiente JSON:

```json
{
  "error": "Usuario no encontrado"
}
```

### Ejemplos

```text
GET /api/usuarios
GET /api/usuarios/1
GET /api/usuarios/Cesar
```

## Próximos pasos sugeridos

La siguiente secuencia permite crecer la API sin añadir complejidad antes de tiempo:

1. Registrar Flask y las futuras dependencias en `requirements.txt`.
2. Sustituir la lista temporal por una base de datos (por ejemplo, SQLite para aprender y PostgreSQL para producción). Así los usuarios no se perderán al reiniciar el servidor.
3. Añadir los métodos `POST`, `PUT`/`PATCH` y `DELETE` para crear, actualizar y eliminar usuarios persistentes.
4. Validar los datos de entrada y añadir pruebas automatizadas para los endpoints.
5. Cuando existan cuentas de usuario y rutas que deban protegerse, implementar autenticación con contraseñas almacenadas de forma segura y tokens JWT. El JWT tiene más sentido después de definir qué recursos requieren permisos y qué roles tendrá cada usuario.
