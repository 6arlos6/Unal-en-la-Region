import geopandas as gpd
import os
from shapely.ops import unary_union
# if no tienen geopandas installa "pip install geopandas"
# path_geo_jSON:
# Tarea_1_Geo_Ref\data_GeoJsons\example.geojson
path_geoJson = os.path.join("Tarea_1_Geo_Ref","data_GeoJsons","example.geojson")
# read file:
gdf = gpd.read_file(path_geoJson)
# identificar regiones: 
region1 = gdf[gdf['nombre_region'] == 'Region1']
region2 = gdf[gdf['nombre_region'] == 'Region2']
# unificar:
region_unida = gpd.GeoDataFrame(geometry=[region1.geometry.unary_union, region2.geometry.unary_union])
# eliminar las anteriores regiones:
gdf = gdf[gdf['nombre_region'] != 'Region1']
gdf = gdf[gdf['nombre_region'] != 'Region2']
# agregar la region unida:
gdf = gdf.append(region_unida, ignore_index=True)
# export:
path_to_save = os.path.join("Tarea_1_Geo_Ref","data_GeoJsons","archivo_unificado.geojson")
gdf.to_file(path_to_save, driver='GeoJSON')
