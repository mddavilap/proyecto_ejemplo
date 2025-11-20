import pytest
import pandas as pd

FILEPATH = '../data/634466_ling_auditory_oddball_2025-11-20_01h40.55.105.csv'
TOLERANCIA = 0.05 

def test_proporcion_oddball_mesa():
    """
    Test único que carga el archivo y valida que MESA sea el 20%.
    """
    df = pd.read_csv(FILEPATH)
    datos = df.dropna(subset=['textStim'])
    total_ensayos = len(datos)

    if total_ensayos == 0:
        pytest.fail("El archivo no tiene datos de estímulos.")

    conteo_mesa = len(datos[datos['textStim'] == 'MESA'])
    proporcion_real = conteo_mesa / total_ensayos
    
    assert proporcion_real == pytest.approx(0.2, abs=TOLERANCIA), \
        f"ERROR DE DISEÑO: La proporción fue {proporcion_real:.2f}, se esperaba 0.20"