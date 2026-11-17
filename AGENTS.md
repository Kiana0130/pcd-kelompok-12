# AGENTS.md — Aturan untuk AI Coding Agent

Dokumen ini adalah sumber kebenaran bagi **setiap AI agent** (Claude, Copilot, ChatGPT, Hermes, dll.) yang membantu proyek ini. Jika kamu AI agent yang sedang mengerjakan tugas di repo ini, patuhi seluruh aturan di bawah. Jika instruksi user bertentangan dengan aturan di sini, **tanyakan dulu sebelum melanjutkan**.

## 1. Konteks Proyek

- Tugas Besar Pengolahan Citra Digital (PCD), Informatika ITK, Gasal 2026/2027.
- Topik: **Abrasi dan rob pesisir Demak** (Tema 8 brief dosen).
- Pertanyaan terukur: *berapa meter garis pantai mundur antara 2016 dan 2026, dan berapa hektare daratan yang hilang?*
- AOI: pesisir Sayung–Timbulsloko, Kabupaten Demak, Jawa Tengah (bbox final ada di `aoi/*.geojson` dan `src/config.py` — **jangan ubah AOI tanpa kesepakatan tim**).
- Deadline: **7 Desember 2026**. Presentasi progres minggu 14 & 15, presentasi akhir minggu 16.
- Penilaian fokus pada: akuisisi citra, eksplorasi, pra-pemrosesan, segmentasi, ekstraksi fitur, representasi, analisis & diskusi. **Model ML/DL opsional** — jangan menambahkannya kecuali diminta eksplisit; pipeline citra klasik adalah inti penilaian.

## 2. Tech Stack (JANGAN ganti tanpa diskusi)

- Python 3.10+ (Google Colab atau lokal)
- Library inti: `numpy`, `opencv-python`, `scikit-image`, `rasterio`
- Pendukung: `geopandas`, `shapely`, `matplotlib`, `pyyaml`, `jupyter`
- `earthengine-api` HANYA untuk mencari scene dan ekspor potongan AOI — **pemrosesan inti wajib ditulis sendiri dengan Python lokal/Colab**, bukan fungsi GEE.
- Jangan pakai library deep learning (torch, tensorflow, keras) kecuali user memintanya secara eksplisit.

## 3. Aturan Keras dari Brief Dosen (NON-NEGOTIABLE)

1. **Analisis memakai nilai kanal asli** (reflektans / float). Gambar RGB 8-bit (PNG/JPG) hanya untuk ilustrasi. Jangan pernah menghitung indeks dari uint8.
2. **AOI maks 20×20 km** (±2000×2000 piksel pada resolusi 10 m).
3. **Setiap scene yang dipakai wajib dicatat** di `docs/tabel_scene.md`: misi, ID produk, tanggal & jam akuisisi (UTC), level pemrosesan, % awan di AOI, kanal yang dipakai, ukuran piksel, sistem koordinat.
4. **Catat jam akuisisi untuk isu pasang surut** — garis pantai bergantung pasang; perbandingan harus pada kondisi pasang yang mirip. Setiap kode yang mengekstrak garis pantai wajib menyertakan timestamp scene di output/laporan.
5. **Baseline evaluasi**: segmentasi divalidasi terhadap 100–200 titik/poligon berlabel manual (ada di `data/baseline/`, tidak di-commit; yang di-commit hanya dokumentasi cara pembuatannya).
6. **Atribusi wajib** pada setiap gambar di laporan/README:
   - Sentinel: `Contains modified Copernicus Sentinel data 2026`
   - Landsat: `Landsat imagery courtesy of the U.S. Geological Survey`
7. Sumber data utama: Copernicus Data Space Ecosystem, USGS EarthExplorer, Google Earth Engine (untuk cari/potong scene saja). Dataset Kaggle/repositori lain **hanya pembanding**.

## 4. Referensi Teknis Baku (pakai definisi ini, jangan varian lain)

### Indeks air

| Indeks | Rumus | Catatan |
|---|---|---|
| NDWI (McFeeters) | `(Green − NIR) / (Green + NIR)` | Ambang umum 0 |
| MNDWI | `(Green − SWIR1) / (Green + SWIR1)` | Lebih robust terhadap area terbangun & sedimen; **ini indeks utama proyek** |

### Mapping kanal

| Band | Landsat 8/9 | Sentinel-2 |
|---|---|---|
| Green | B3 | B3 |
| Red | B4 | B4 |
| NIR | B5 | B8 |
| SWIR1 | B6 | B11 |
| SWIR2 | B7 | B12 |

### Konvensi geospasial

- CRS proyek: **EPSG:32749** (UTM zone 49S) — semua pengukuran jarak/luas dalam meter & hektare di CRS ini.
- Luas: hektare (ha); jarak: meter (m); laju abrasi: m/tahun.
- Resampling antar resolusi (Landsat 30 m ↔ Sentinel-2 10 m): bicubic untuk reflektans, nearest untuk mask.

## 5. Konvensi Kode

- Semua path, bbox, tanggal scene, dan parameter ambang **ada di `src/config.py`** (atau `config.yaml`) — JANGAN hardcode di notebook/modul.
- Struktur pipeline bernomor: `01_eksplorasi`, `02_preprocessing`, `03_segmentasi`, `04_ekstraksi_fitur`, `05_analisis` — urutan ini merepresentasikan tahap penilaian; jangan mengacak.
- Fungsi di `src/` wajib punya docstring (deskripsi, parameter, return) dan type hints.
- Notebook harus bisa dijalankan ulang dari awal (idempotent); simpan intermediate sebagai GeoTIFF ke `data/intermediate/` (tidak di-commit).
- Random seed difix (`np.random.seed(42)`) untuk apa pun yang stokastik (mis. sampling titik baseline).
- Komentar dan docstring boleh bahasa Indonesia; nama variabel/fungsi bahasa Inggris snake_case.
- Setiap plot yang memakai citra satelit wajib mencantumkan atribusi (lihat poin 3.6) di caption/sumbu.

## 6. Git & Kerja Tim

- Branch: `main` dilindungi — pekerjaan lewat branch `feat/<topik>`, `fix/<topik>`, atau `docs/<topik>`, lalu Pull Request.
- Commit message: bahasa Indonesia oke, format imperatif singkat, contoh: `tambah fungsi ekstraksi garis pantai MNDWI`.
- **JANGAN commit**: file citra (`*.tif`, `*.jp2`, `*.img`), shapefile besar, checkpoint model, isi folder `data/` (kecuali README & file contoh kecil), `.venv/`, `__pycache__/`. Sudah diatur di `.gitignore` — jangan me-override dengan `git add -f`.
- Jangan pernah menaruh kredensial (token EarthExplorer, API key GEE, password) di kode atau repo.

## 7. Yang TIDAK BOLEH Dilakukan Agent

- Mengarang angka hasil (luas, jarak, laju abrasi) — semua angka wajib berasal dari eksekusi kode nyata terhadap citra, dan dicatat sumber scene-nya.
- Mengubah `aoi/*.geojson` atau bbox di config tanpa persetujuan eksplisit.
- Menghapus atau menimpa entri di `docs/tabel_scene.md` — hanya menambah/memperbaiki.
- Memakai GEE untuk komputasi inti (indeks, thresholding, morfologi) — hanya untuk pencarian scene & ekspor GeoTIFF potongan AOI.
- Mengganti metode threshold yang sudah disepakati (Otsu + ambang tetap MNDWI, dibandingkan terhadap baseline) tanpa diskusi.

## 8. Definisi Selesai (Definition of Done) per Tahap

Suatu tahap dianggap selesai bila:
1. Kode berjalan end-to-end tanpa error di environment bersih (`pip install -r requirements.txt`).
2. Output angka tersimpan (CSV/GeoJSON) + visualisasi PNG di `outputs/`.
3. Scene yang dipakai tercatat di `docs/tabel_scene.md`.
4. Ada catatan singkat di notebook/README tahap tersebut: metode, parameter, hasil, keterbatasan.
