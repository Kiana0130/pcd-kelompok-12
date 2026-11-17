# AOI (Area of Interest)

Simpan batas AOI final sebagai **GeoJSON** di folder ini (wajib di-commit sesuai brief), contoh: `aoi/sayung_timbulsloko.geojson`.

- AOI maks ~20×20 km
- CRS GeoJSON: EPSG:4326
- Usulan awal: pesisir Sayung–Timbulsloko, Demak (bbox ada di `src/config.py`)
- Sebelum final: cek ketersediaan scene Landsat 2016 & Sentinel-2 2026 yang minim awan di bbox ini

Buat GeoJSON bisa dari [geojson.io](https://geojson.io) (gambar poligon → Save → GeoJSON) atau dengan Python:

```python
import geopandas as gpd
from shapely.geometry import box
from src.config import AOI_BBOX, CRS_GEO

gdf = gpd.GeoDataFrame(
    geometry=[box(AOI_BBOX["west"], AOI_BBOX["south"],
                  AOI_BBOX["east"], AOI_BBOX["north"])],
    crs=CRS_GEO,
)
gdf.to_file("aoi/sayung_timbulsloko.geojson", driver="GeoJSON")
```
