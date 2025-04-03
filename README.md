# API Demo con FastAPI

Proyecto simple de API construida con FastAPI.

## Instalación

1. Crear un entorno virtual:
   ```
   python3 -m venv venv
   ```
2. Activar el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En macOS/Linux: `source venv/bin/activate`
3. Instalar dependencias:
   ```
   uv pip install -e .
   ```

## Ejecutar la aplicación

Para iniciar el servidor de desarrollo:

```
uvicorn app.main:app --reload
```

La aplicación estará disponible en [http://localhost:8000](http://localhost:8000)

## Documentación de la API

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc) 