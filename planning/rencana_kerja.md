# Rencana Kerja 3 Minggu — Tim 3 Orang

Deadline: **7 Desember 2026**. Presentasi progres asprak: minggu 14 & 15. Presentasi akhir: minggu 16.

> Prinsip: setiap orang **penanggung jawab utama** satu area, tapi pipeline dikerjakan bersama lewat PR. Semua tahap mengikuti urutan penilaian brief: akuisisi → eksplorasi → pra-pemrosesan → segmentasi → ekstraksi fitur → representasi → analisis.

## Minggu 1 (17–23 Nov) — Data & Fondasi

**Target: AOI final, semua scene terunduh & terdokumentasi, lingkungan kerja jalan.**

- [ ] Sepakati AOI final (cek dulu ketersediaan Landsat 2016 & S2 2026 minim awan di bbox usulan) → simpan GeoJSON di `aoi/`
- [ ] Buat akun USGS EarthExplorer + Copernicus (semua anggota)
- [ ] Unduh scene Landsat 8/9: minimal 2016 & 2026 (+ 2021 jika memungkinkan) → `data/raw/landsat/`
- [ ] Unduh/export Sentinel-2 L2A 2026 (potongan AOI GeoTIFF via Copernicus Browser) → `data/raw/sentinel2/`
- [ ] Isi `docs/tabel_scene.md` untuk SEMUA scene (termasuk jam UTC untuk isu pasang!)
- [ ] Buat folder Drive tim, tautkan di `data/README.md`
- [ ] Notebook `01_eksplorasi`: tampilkan citra, histogram kanal, cek tutupan awan, hitung MNDWI pertama kali → sanity check daratan/air masuk akal
- [ ] **Checkpoint minggu 14**: siap presentasi progres (AOI, tabel scene, hasil MNDWI awal)

## Minggu 2 (24–30 Nov) — Pipeline Inti

**Target: garis pantai 2016 & 2026 berhasil diekstrak, baseline validasi jadi.**

- [ ] `src/`: fungsi crop AOI, konversi reflektans (jika perlu), resample Landsat↔S2
- [ ] `src/`: hitung NDWI & MNDWI dari kanal asli (float!)
- [ ] `src/`: thresholding — Otsu + ambang tetap MNDWI (0.0), bandingkan keduanya
- [ ] Morfologi (opening/closing) untuk bersihkan noise di mask air
- [ ] Buat baseline 100–200 titik/poligon label manual → `data/baseline/`, dokumentasikan cara pembuatan di `docs/baseline.md`
- [ ] Evaluasi segmentasi vs baseline (akurasi/IoU per metode threshold)
- [ ] Deteksi tepi (Canny/`find_contours`) → vektor garis pantai per tahun, simpan GeoJSON
- [ ] **Checkpoint minggu 15**: siap presentasi progres (mask tervalidasi + garis pantai terekstrak)

## Minggu 3 (1–7 Des) — Fitur, Analisis, Laporan

**Target: angka final + laporan + slides.**

- [ ] Representasi garis pantai: chain code & deskriptor Fourier (per kontur)
- [ ] Jarak antargaris pantai 2016→2026: transek tegak lurus / jarak titik-ke-garis → statistik (mundur rata-rata, maksimum, per segmen)
- [ ] Selisih luas daratan → hektare hilang (di EPSG:32749)
- [ ] Laju abrasi m/tahun; jika ada 2021 → grafik tren
- [ ] Diskusi: pengaruh pasang surut (jam akuisisi!), rob, mangrove Timbulsloko, pembanding berita
- [ ] Rapikan `outputs/` (PNG + atribusi di setiap gambar), tulis laporan akhir
- [ ] Latihan presentasi; slide mencakup pipeline diagram & angka kunci

## Pembagian Penanggung Jawab

| Area | PJ | Backup |
|---|---|---|
| Akuisisi data, tabel scene, isu pasang surut | *(nama)* | *(nama)* |
| Pra-pemrosesan & segmentasi (indeks, threshold, morfologi, baseline) | *(nama)* | *(nama)* |
| Ekstraksi fitur & analisis (kontur, chain code, Fourier, jarak, luas) | *(nama)* | *(nama)* |
| Laporan & slide | Bersama (draft: semua, editor: bergilir) | |

## Aturan main

- Kerja lewat branch + PR, minimal 1 review sebelum merge (lihat `docs/GETTING_STARTED.md`).
- Update checklist file ini setiap selesai item (centang `[x]`) — biar progres terlihat untuk presentasi asprak.
- Mentok > 30 menit di satu hal? Post di grup, jangan diam.
