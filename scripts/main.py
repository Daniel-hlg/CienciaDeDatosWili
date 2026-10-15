from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI(
    title="API Servicio de Emprendimiento SENA",
    description="API RESTful simulada para la gestión de emprendedores y sus proyectos vinculados.",
    version="1.0.0"
)

# ==========================================
# TABLAS SIMULADAS (Base de datos en JSON)
# ==========================================

# Tabla 1: Emprendedores
EMPRENDEDORES_DB = [
    {
        "id": 1,
        "nombre": "Daniel Holguín",
        "correo": "daniel.holguin@soy.sena.edu.co",
        "telefono": "3001234567",
        "unidad_productiva": "Fondo Emprender CTMA"
    },
    {
        "id": 2,
        "nombre": "María Fernanda Gómez",
        "correo": "m.gomez@soy.sena.edu.co",
        "telefono": "3119876543",
        "unidad_productiva": "SENA Emprende Rural"
    },
    {
        "id": 3,
        "nombre": "Carlos Andrés Pérez",
        "correo": "c.perez@soy.sena.edu.co",
        "telefono": "3205554433",
        "unidad_productiva": "TecnoParque Medellín"
    }
]

# Tabla 2: Proyectos (Relacionada con Emprendedores mediante 'id_emprendedor')
PROYECTOS_DB = [
    {
        "id": 101,
        "titulo": "Empanadas Don Sabor",
        "categoria": "Alimentos y Bebidas",
        "estado": "En formulación",
        "presupuesto_solicitado": 15000000.0,
        "id_emprendedor": 1
    },
    {
        "id": 102,
        "titulo": "Plataforma IoT para Cultivos",
        "categoria": "Agrotech",
        "estado": "Aprobado",
        "presupuesto_solicitado": 28000000.0,
        "id_emprendedor": 2
    },
    {
        "id": 103,
        "titulo": "App Móvil de Gestión de Mantenimiento",
        "categoria": "Software y TIC",
        "estado": "En evaluación",
        "presupuesto_solicitado": 20000000.0,
        "id_emprendedor": 1
    }
]

# ==========================================
# ENDPOINTS / RUTAS
# ==========================================

@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "Bienvenido a la API del Servicio de Emprendimiento SENA",
        "documentacion": "/docs"
    }

# ------------------------------------------
# ENDPOINTS DE EMPRENDEDORES (TABLA 1)
# ------------------------------------------

@app.get("/emprendedores", tags=["Emprendedores"])
def obtener_todos_los_emprendedores():
    """Retorna el listado completo de emprendedores registrados."""
    return {"total": len(EMPRENDEDORES_DB), "datos": EMPRENDEDORES_DB}


@app.get("/emprendedores/{emprendedor_id}", tags=["Emprendedores"])
def obtener_emprendedor_por_id(emprendedor_id: int):
    """Consulta los datos de un emprendedor uno a uno buscando por su ID."""
    for emp in EMPRENDEDORES_DB:
        if emp["id"] == emprendedor_id:
            # Buscamos los proyectos asociados a este emprendedor (Relación)
            proyectos_asociados = [
                p for p in PROYECTOS_DB if p["id_emprendedor"] == emprendedor_id
            ]
            
            resultado = emp.copy()
            resultado["proyectos_asociados"] = proyectos_asociados
            return resultado
            
    raise HTTPException(
        status_code=404, 
        detail=f"Emprendedor con ID {emprendedor_id} no encontrado."
    )

# ------------------------------------------
# ENDPOINTS DE PROYECTOS (TABLA 2)
# ------------------------------------------

@app.get("/proyectos", tags=["Proyectos"])
def obtener_todos_los_proyectos():
    """Retorna el listado completo de proyectos de emprendimiento."""
    return {"total": len(PROYECTOS_DB), "datos": PROYECTOS_DB}


@app.get("/proyectos/{proyecto_id}", tags=["Proyectos"])
def obtener_proyecto_por_id(proyecto_id: int):
    """Consulta los datos de un proyecto uno a uno buscando por su ID."""
    for proy in PROYECTOS_DB:
        if proy["id"] == proyecto_id:
            # Buscamos la información del emprendedor dueño del proyecto (Relación)
            emprendedor_dueno = next(
                (e for e in EMPRENDEDORES_DB if e["id"] == proy["id_emprendedor"]), 
                None
            )
            
            resultado = proy.copy()
            resultado["emprendedor"] = emprendedor_dueno
            return resultado

    raise HTTPException(
        status_code=404, 
        detail=f"Proyecto con ID {proyecto_id} no encontrado."
    )