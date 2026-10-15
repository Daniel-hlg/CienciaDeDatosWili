# Ciencia de Datos con Python - Semana 1

## Propósito
Preparar un ambiente de trabajo reproducible y comprender el valor de los datos para apoyar la toma de decisiones en proyectos de formación y entorno productivo.

## Estructura del Proyecto
- `data/raw`: Datos originales (únicamente lectura).
- `data/processed`: Datos procesados y limpios.
- `notebooks`: Ejercicios, análisis exploratorio y bitácoras de aprendizaje.
- `outputs`: Reportes, gráficos y archivos exportados.
- `docs`: Documentación del proyecto.
- `scripts`: Código Python reutilizable.

## Buenas Prácticas
1. No modificar directamente los datos originales (`data/raw`).
2. Documentar cada decisión analítica y transformación relevante.
3. Proteger datos personales respetando la privacidad y normatividad ética (Habeas Data).
4. Usar rutas relativas para garantizar la reproducibilidad.
5. Mantener los notebooks limpios, ordenados y comentados.

## Instrucciones de Ejecución
1. Activar el entorno virtual:
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Linux / macOS: `source .venv/bin/activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar el notebook de verificación en `notebooks/semana_01_contexto_ambiente.ipynb`.