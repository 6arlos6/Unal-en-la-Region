import pandas as pd
import geopandas as gpd
import os
from shapely.ops import unary_union


def unir_regiones(gdf_municipios, df_sub_reg, departamento_name, tf_save = False, path_to_save = None):
    '''[Su descripcion.]

    :param gdf_municipios: objeto geopandas con municipios, defaults to <Sin valor por defecto>
    :type gdf_municipios: objeto geopandas

    :param df_sub_reg: dataframe pandas con info de subregiones, defaults to <Sin valor por defecto>
    :type df_sub_reg: DataFramePandas

    :param departamento_name: nombre del departamento objetivo, defaults to <Sin valor por defecto>
    :type departamento_name: str

    :param tf_save: opcion para guardar el gdf_subregiones, defaults to False
    :type tf_save: boolean 

    :param path_to_save: path para guardar gdf_subregiones, defaults to None
    :type path_to_save: str
   
    :return: gdf_subregiones
    :rtype: objeto geopandas
    '''
    # ====== PASOS REQUERIDOS ======= #
    # paso 1. filtrar gdf_municipios por departamento con departamento_name
    # paso 2. obtener municipios del filtrado anterior.
    # paso 3. por cada una de las sub regiones df_sub_reg obtener de gdf_municipio_filtrado las geometrias...
    # paso 4. unir los municipios y ponerle nombre de sub reguion de df_sub_reg y guardarlo en gdf_subregiones
    # paso 5. si tf_save = True...
    # paso 6. guardar el gdf_subregiones en la direccion path_to_save
    return 1


if __name__ == '__main__':
    print("Hola")

