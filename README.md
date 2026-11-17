# Abrasi & Rob Pesisir Demak — Tubes PCD 2026

Pipeline pengolahan citra penginderaan jauh untuk mengukur **kemunduran garis pantai dan kehilangan daratan di pesisir Demak (Sayung–Timbulsloko) antara 2016 dan 2026**.

Tugas Besar mata kuliah **Pengolahan Citra Digital (PCD)**, Semester Gasal 2026/2027 — Informatika ITK.

## Konteks

Pada 7 Oktober 2026 pemerintah mengumumkan proyek tanggul laut pantura sepanjang 575 km akan dimulai dengan penanaman mangrove di Desa Timbulsloko, Demak (sumber: Katadata). Proyek ini menjawab pertanyaan terukur:

> **Berapa meter garis pantai mundur antara 2016 dan 2026, dan berapa hektare daratan yang hilang?**

## Tim

| Nama | NIM | Peran utama |
|---|---|---|
| *(isi)* | *(isi)* | Akuisisi data & dokumentasi scene |
| *(isi)* | *(isi)* | Pra-pemrosesan & segmentasi |
| *(isi)* | *(isi)* | Ekstraksi fitur & analisis |

*(peran hanya penanggung jawab utama — semua anggota mengerjakan pipeline bersama)*

## Struktur Repository

| Path | Isi |
|---|---|
| `AGENTS.md` | Aturan main untuk AI coding agent — **baca dulu sebelum minta bantuan AI apa pun** |
| `src/` | Kode pipeline (modul Python yang dipakai bersama) |
| `notebooks/` | Notebook per tahap: eksplorasi → pra-pemrosesan → segmentasi → ekstraksi fitur → analisis |
| `aoi/` | Batas AOI (GeoJSON) — wajib ada di repo sesuai brief |
| `data/` | **Tidak di-commit.** Citra mentah & olahan disimpan di folder Drive tim |
| `docs/` | Dokumentasi: tabel scene, panduan kerja tim (GETTING_STARTED) |
| `outputs/` | Gambar/ilustrasi PNG untuk laporan (bukan untuk analisis) |
| `planning/` | Rencana kerja 3 minggu |

## Pipeline (ringkas)

1. **Akuisisi** — Landsat 8/9 (USGS EarthExplorer) untuk deret 2016–2026, Sentinel-2 L2A (Copernicus) untuk detail 10 m
2. **Pra-pemrosesan** — crop AOI, mask awan, konversi ke reflektans, penyamaan CRS
3. **Segmentasi** — NDWI/MNDWI → thresholding (Otsu & ambang tetap, dibandingkan terhadap baseline manual) → morfologi
4. **Ekstraksi fitur** — deteksi tepi → garis pantai sebagai kontur → representasi (chain code, deskriptor Fourier)
5. **Analisis** — jarak antargaris pantai (m), selisih luas daratan (ha), laju kemunduran (m/tahun), diskusi pengaruh pasang surut

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ketentuan Data (dari brief — WAJIB dipatuhi)

- AOI maks ~20×20 km; batas AOI disimpan sebagai GeoJSON di `aoi/`
- Minimal 2 waktu akuisisi (sebelum–sesudah / beda tahun)
- Analisis memakai **nilai kanal asli (reflektans)**, bukan PNG/JPG 8-bit
- Setiap scene didokumentasikan di `docs/tabel_scene.md`
- Baseline evaluasi: 100–200 titik/poligon berlabel hasil interpretasi visual

## Atribusi

- Sentinel: *"Contains modified Copernicus Sentinel data 2026"*
- Landsat: *"Landsat imagery courtesy of the U.S. Geological Survey"*
