# Tabel Dokumentasi Scene

Wajib diisi untuk **setiap scene yang dipakai** (ketentuan akuisisi poin 3 di brief). Tambah baris baru, jangan menghapus yang sudah ada.

| # | Misi | ID Produk | Tanggal & Jam Akuisisi (UTC) | Level | % Awan di AOI | Kanal Dipakai | Ukuran Piksel (m) | CRS | Kondisi Pasang* | Pengunduh |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Landsat 8 | *(mis. LC08_L2SP_119065_20160815_20200908_02_T1)* | *(2016-08-15 03:00)* | L2 SP (SR) | *(isi)* | B3, B5, B6 | 30 | EPSG:32749 | *(cek jam vs prediksi pasang)* | *(nama)* |
| 2 | | | | | | | | | | |

\* **Kolom kondisi pasang penting untuk topik kita**: garis pantai bergantung pasang surut. Cara mengisi: lihat jam akuisisi scene, cek prediksi pasang surut Pelabuhan Semarang/Demak pada tanggal-jam tersebut (sumber mis. data BIG atau model pasang global seperti tide-model.io / FES), catat perkiraan tinggi pasang (mis. "pasang tinggi ~0.9 m" atau "surut ~0.2 m"). Bandingkan hanya scene dengan kondisi pasang mirip, dan bahas di analisis.

## Catatan akuisisi

- Sumber: USGS EarthExplorer (Landsat 8/9 Collection 2), Copernicus Browser (Sentinel-2 L2A), GEE hanya untuk cari scene/potong AOI.
- Path WRS-2 Landsat untuk Demak: sekitar **path 119 row 065** (verifikasi saat mencari).
- Sentinel-2 tile MGRS untuk Demak: sekitar **49MFM / 49MGN** (verifikasi).
