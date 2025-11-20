import pytest
import sys
import os

# Agregamos la carpeta raíz al path para poder importar utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import calcular_estadisticas, procesar_texto, operacion_compleja

def test_calcular_estadisticas_basico():
    datos = [10, 20, 30]
    resultado = calcular_estadisticas(datos)
    assert resultado['suma'] == 60
    assert resultado['promedio'] == 20

def test_calcular_estadisticas_vacia():
    datos = []
    assert calcular_estadisticas(datos) is None

def test_procesar_texto():
    texto = "  HOLA MUNDO  "
    assert procesar_texto(texto) == "hola mundo"

def test_operacion_compleja_exito():
    assert operacion_compleja(2, 3, 4) == 10  # (2*3)+4 = 10

def test_operacion_compleja_error(capsys):
    # Pasamos un string para forzar el error en la multiplicación
    operacion_compleja(2, "texto", 4) 
    captured = capsys.readouterr()
    # Verificamos que imprimió el mensaje del 'except'
    assert "Ocurrio un error" in captured.out