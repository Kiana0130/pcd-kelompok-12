"""Konfigurasi terpusat proyek Tubes PCD — Abrasi & Rob Pesisir Demak.

SEMUA path, bbox, tanggal scene, dan parameter pipeline diambil dari sini.
Jangan hardcode nilai-nilai ini di notebook atau modul lain.
Lihat AGENTS.md sebelum mengubah file ini.
"""

from pathlib import Path

# === Path ===
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"                 # citra mentah (dari Drive, tidak di-commit)
INTERMEDIATE_DIR = DATA_DIR / "intermediate"
BASELINE_DIR = DATA_DIR / "baseline"       # titik/poligon label manual
AOI_DIR = ROOT / "aoi"
OUTPUT_DIR = ROOT / "outputs"

# === AOI: pesisir Sayung–Timbulsloko, Demak ===
# CATATAN: bbox ini USULAN awal — verifikasi dulu ketersediaan scene Landsat 2016
# dan Sentinel-2 2026 yang minim awan sebelum difinalkan, lalu simpan sebagai
# GeoJSON di aoi/ dan update nilai di sini. Maks 20x20 km (aturan brief).
# Batas saat ini kira-kira 11 x 11 km.
AOI_BBOX = {
    "west": 110.48,
    "south": -6.95,
    "east": 110.58,
    "north": -6.85,
}
AOI_NAME = "sayung_timbulsloko"

# === CRS ===
# UTM zone 49S — wilayah Demak. Semua pengukuran jarak (m) & luas (ha) di CRS ini.
CRS_METRIC = "EPSG:32749"
CRS_GEO = "EPSG:4326"

# === Periode analisis ===
YEAR_BASELINE = 2016   # garis pantai awal
YEAR_TARGET = 2026     # garis pantai akhir
# Opsional: tahun antara untuk tren (mis. [2016, 2021, 2026])
YEARS_SERIES = [2016, 2026]

# === Mapping kanal (lihat AGENTS.md bagian 4) ===
# Landsat 8/9 (SR, Collection 2)
LANDSAT_BANDS = {"green": "SR_B3", "red": "SR_B4", "nir": "SR_B5",
                 "swir1": "SR_B6", "swir2": "SR_B7"}
# Sentinel-2 L2A
S2_BANDS = {"green": "B03", "red": "B04", "nir": "B08",
            "swir1": "B11", "swir2": "B12"}

# === Indeks ===
PRIMARY_INDEX = "MNDWI"   # (Green - SWIR1) / (Green + SWIR1)
MNDWI_THRESHOLD_FIXED = 0.0   # ambang tetap pembanding Otsu

# === Baseline evaluasi ===
BASELINE_N_POINTS = 150   # target 100-200 titik/poligon label manual
RANDOM_SEED = 42

# === Atribusi wajib ===
ATTRIBUTION_SENTINEL = "Contains modified Copernicus Sentinel data 2026"
ATTRIBUTION_LANDSAT = "Landsat imagery courtesy of the U.S. Geological Survey"
