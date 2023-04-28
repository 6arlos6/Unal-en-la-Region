# !pip install geopandas
import geopandas as gpd
import os
from shapely.ops import cascaded_union

# cargar:
# data_GeoJsons\map.geojson
path_geoJson = os.path.join("data_GeoJsons","map.geojson")
# read file:
gdf = gpd.read_file(path_geoJson)
# poner nombre a las regiones:
gdf["nombre_region"] = ["Region1","Region2"]
# identificar regiones: 
region1 = gdf[gdf['nombre_region'] == 'Region1']
region2 = gdf[gdf['nombre_region'] == 'Region2']
# unificar:
region_unida = gpd.GeoSeries(cascaded_union([region1["geometry"],
                                             region2["geometry"]]))
# agregar la region unida:
gdf = gdf.append(region_unida, ignore_index=True)
# eliminar las anteriores regiones:
gdf = gdf[gdf['nombre_region'] != 'Region1']
gdf = gdf[gdf['nombre_region'] != 'Region2']
# poner nombre a la region unida:
gdf["nombre_region"] = "Region_Unida"
# crear una col. llamada geometry donde va el poligono generado por la region unida
gdf["geometry"] = gdf[0]
# eliminar col por defecto que se creo al unir las regiones
gdf  = gdf.drop(columns=0)
# export:
path_to_save = os.path.join("data_GeoJsons","archivo_unificado.geojson")
gdf.to_file(path_to_save, driver='GeoJSON')