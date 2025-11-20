import math
import sys, os  # Flake8: Imports no usados (F401) y múltiples en una línea

def calcular_estadisticas( data ): # Black: Espacios innecesarios dentro de paréntesis
    """Calcula suma y promedio."""
    if len(data)==0: return None  # Black: If en una línea (E701) y falta espacios en operador (E225)
    
    total=sum(data) # Black: Falta espacio alrededor del =
    promedio = total/len(data)
    
    variable_inutil = 100  # Flake8: Variable asignada pero nunca usada (F841)

    # Flake8: Línea demasiado larga (>79 caracteres) (E501)
    resultado = {'suma': total, 'promedio': promedio, 'status': "ok", 'metadata': "calculado automaticamente por el sistema"} 
    
    return resultado

def procesar_texto(texto):
    # Black: Convertirá comillas simples a dobles
    # Flake8: Comparación con True/False es mala práctica (E712), debe ser 'if texto:' o 'if es_valido:'
    es_valido = True
    if es_valido == True: 
        limpio = texto.strip().lower()
        return limpio

def operacion_compleja(x,y, z): # Black: Falta espacio después de coma
    try:
        # Black: Añadirá espacios en la operación matemática
        res=(x*y)+z 
        return res
    except:  # Flake8: No usar 'except' desnudo (E722), debe ser 'except Exception:' o específico
        print("Ocurrio un error")

def lista_gigante():
    # Black: Romperá esta lista en múltiples líneas (Trailing comma)
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    return lista