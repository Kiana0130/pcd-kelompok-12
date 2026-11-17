# Kandidat Scene — Hasil Pengecekan Katalog (17 Nov 2026)

Pengecekan ketersediaan citra pada AOI usulan **bbox [110.48, -6.95, 110.58, -6.85]** (Sayung–Timbulsloko, ±11×11 km — memenuhi batas 20×20 km) via katalog publik AWS Earth Search (STAC). Hasil: **AOI layak**, scene tersedia melimpah untuk semua periode.

Fakta penting:
- Landsat WRS-2 untuk AOI ini: **path 120, row 065**
- Sentinel-2 tile MGRS: **49MDN**
- Jam akuisisi Landsat konsisten **±02:47–02:51 UTC** (≈10:47–10:51 WIB) dan Sentinel-2 **±03:00 UTC** → kondisi pasang relatif sebanding antar scene; tetap wajib diverifikasi per tanggal (lihat `tabel_scene.md`).

## Rekomendasi pasangan utama (musim kemarau, bulan berdekatan)

| Peran | Scene | Tanggal (UTC) | Cloud | Catatan |
|---|---|---|---|---|
| **Baseline 2016** | `LE07_L2SP_120065_20160811_02_T1` | 2016-08-11 02:50:44 | 3% | ⚠️ Landsat 7 SLC-off: ada strip/garis kosong ±22% — wajib di-mask/ditambal |
| Backup 2016 | `LC08_L2SP_120065_20160819_02_T1` | 2016-08-19 02:48:13 | 16.2% | Landsat 8, tanpa masalah SLC-off; cek cloud khusus di AOI |
| **Target 2026** | `LC09_L2SP_120065_20260807_02_T1` | 2026-08-07 02:47:56 | 6.0% | Landsat 9, bulan sama dengan baseline (Agustus) |
| Backup 2026 | `LC09_L2SP_120065_20260924_02_T1` | 2026-09-24 02:48:09 | 1.9% | Cloud terendah 2026 |
| Tengah 2021 (opsional, untuk tren) | `LC08_L2SP_120065_20210817_02_T1` | 2021-08-17 02:48:16 | 7.5% | Agustus juga; alternatif LE07 2021-07-24 (3%, SLC-off) |
| **Detail 10 m (2026)** | `S2B_49MDN_20260825_0_L2A` | 2026-08-25 02:59:49 | 0.4% | Sentinel-2 L2A; alternatif S2B 2026-07-26 (0.3%) |

## Top 8 per periode (cloud terendah)

### Landsat 2016 (19 scene cloud<40%)
| Cloud | Tanggal (UTC) | Musim | ID |
|---|---|---|---|
| 3.00% | 2016-08-11 02:50:44 | kemarau | LE07_L2SP_120065_20160811_02_T1 |
| 5.00% | 2016-07-10 02:50:40 | kemarau | LE07_L2SP_120065_20160710_02_T1 |
| 10.98% | 2016-03-28 02:47:49 | hujan | LC08_L2SP_120065_20160328_02_T1 |
| 11.00% | 2016-06-24 02:50:41 | kemarau | LE07_L2SP_120065_20160624_02_T1 |
| 11.00% | 2016-08-27 02:50:47 | kemarau | LE07_L2SP_120065_20160827_02_T1 |
| 14.81% | 2016-01-08 02:48:11 | hujan | LC08_L2SP_120065_20160108_02_T1 |
| 16.23% | 2016-08-19 02:48:13 | kemarau | LC08_L2SP_120065_20160819_02_T1 |
| 20.40% | 2016-04-29 02:47:42 | hujan | LC08_L2SP_120065_20160429_02_T1 |

### Landsat 2021 (20 scene cloud<40%) — opsional untuk tren
| Cloud | Tanggal (UTC) | Musim | ID |
|---|---|---|---|
| 3.00% | 2021-07-24 01:50:14 | kemarau | LE07_L2SP_120065_20210724_02_T1 |
| 7.45% | 2021-08-17 02:48:16 | kemarau | LC08_L2SP_120065_20210817_02_T1 |
| 7.77% | 2021-04-27 02:47:42 | hujan | LC08_L2SP_120065_20210427_02_T1 |
| 8.00% | 2021-05-21 01:55:37 | transisi | LE07_L2SP_120065_20210521_02_T1 |
| 9.35% | 2021-09-18 02:48:25 | kemarau | LC08_L2SP_120065_20210918_02_T1 |
| 12.00% | 2021-04-19 01:58:18 | hujan | LE07_L2SP_120065_20210419_02_T1 |
| 14.00% | 2021-03-18 02:00:56 | hujan | LE07_L2SP_120065_20210318_02_T1 |
| 17.00% | 2021-06-06 01:54:15 | kemarau | LE07_L2SP_120065_20210606_02_T1 |

### Landsat 2026 (27 scene cloud<40%, sampai 17 Nov)
| Cloud | Tanggal (UTC) | Musim | ID |
|---|---|---|---|
| 1.85% | 2026-09-24 02:48:09 | kemarau | LC09_L2SP_120065_20260924_02_T1 |
| 2.20% | 2026-07-14 02:47:32 | kemarau | LC08_L2SP_120065_20260714_02_T1 |
| 4.26% | 2026-06-20 02:47:31 | kemarau | LC09_L2SP_120065_20260620_02_T1 |
| 5.48% | 2026-07-06 02:47:38 | kemarau | LC09_L2SP_120065_20260706_02_T1 |
| 5.80% | 2026-10-02 02:48:08 | transisi | LC08_L2SP_120065_20261002_02_T1 |
| 5.97% | 2026-08-07 02:47:56 | kemarau | LC09_L2SP_120065_20260807_02_T1 |
| 7.81% | 2026-06-28 02:47:28 | kemarau | LC08_L2SP_120065_20260628_02_T1 |
| 8.03% | 2026-06-04 02:47:21 | kemarau | LC09_L2SP_120065_20260604_02_T1 |

### Sentinel-2 L2A 2026 (50 scene cloud<40%, sampai 17 Nov)
| Cloud | Tanggal (UTC) | Musim | ID |
|---|---|---|---|
| 0.00% | 2026-10-14 02:59:51 | transisi | S2B_49MDN_20261014_0_L2A |
| 0.10% | 2026-06-11 02:59:52 | kemarau | S2C_49MDN_20260611_0_L2A |
| 0.33% | 2026-07-26 02:59:53 | kemarau | S2B_49MDN_20260726_0_L2A |
| 0.39% | 2026-09-14 02:59:50 | kemarau | S2B_49MDN_20260914_0_L2A |
| 0.43% | 2026-08-25 02:59:49 | kemarau | S2B_49MDN_20260825_0_L2A |
| 1.01% | 2026-10-01 03:00:05 | transisi | S2A_49MDN_20261001_0_L2A |
| 1.29% | 2026-09-29 02:59:53 | kemarau | S2C_49MDN_20260929_0_L2A |
| 1.32% | 2026-08-02 03:00:10 | kemarau | S2A_49MDN_20260802_0_L2A |

## Catatan

1. **% cloud di atas adalah nilai seluruh scene**, bukan khusus AOI — saat mengunduh, cek ulang % cloud di atas AOI dan catat di `tabel_scene.md`.
2. **SLC-off Landsat 7**: scene `LE07` pasca-2003 punya strip data hilang. Kalau dipakai, tambahkan langkah mask/tambal (mis. gabung dua scene berdekatan tanggalnya, atau interpolasi) dan bahas sebagai keterbatasan. Alternatif aman: pakai scene `LC08`.
3. Katalog AWS dipakai **hanya untuk survei ketersediaan**. Unduhan resmi untuk tugas: USGS EarthExplorer (Landsat) dan Copernicus Browser (Sentinel-2) sesuai brief — ID scene di atas bisa dipakai langsung untuk pencarian di sana.
4. Keputusan akhir pasangan scene → diskusikan bertiga, lalu isi baris di `tabel_scene.md`.
