"""
Modulo de Modelos - Producto
Define las entidades principales del sistema, adaptadas para una Botica.
"""
from datetime import datetime
from enum import Enum

class Categoria(Enum):
    """Enumeracion de categorias de productos en una Botica (Farmacia)."""
    MEDICAMENTOS_CON_RECETA = "Medicamentos con Receta"
    MEDICAMENTOS_LIBRE_VENTA = "Medicamentos de Venta Libre"
    CUIDADO_PERSONAL = "Cuidado Personal"
    SUPLEMENTOS = "Vitaminas y Suplementos"
    MATERIAL_CURACION = "Material de Curacion"
    BEBES_Y_NINOS = "Bebés y Niños"
    OTROS = "Otros Productos de Botica"

class Producto:
    """
    Representa un producto en el inventario de la botica.

    Attributes:
        id_producto (int): Identificador unico
        nombre (str): Nombre del producto (ej: Paracetamol, Pañales)
        descripcion (str): Descripcion del producto
        precio (float): Precio unitario
        cantidad (int): Cantidad en stock
        categoria (Categoria): Categoria del producto
        fecha_creacion (str): Fecha de creacion
    """
    
    _contador = 1000