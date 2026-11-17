# Folder Data (TIDAK di-commit ke Git)

Isi folder ini di-ignore oleh Git karena file citra berukuran besar. **Simpan semua data di folder Drive tim**, lalu setiap anggota mengunduh/sinkronkan ke struktur lokal yang sama:

```
data/
├── raw/                  # citra mentah unduhan (Landsat/Sentinel-2 GeoTIFF)
│   ├── landsat/          # mis. LC08_L2SP_119065_20160815_...
│   └── sentinel2/        # mis. S2A_MSIL2A_20260710T...
├── intermediate/         # hasil crop/mask/indeks (GeoTIFF olahan)
└── baseline/             # titik/poligon label manual (GeoJSON/CSV)
```

Aturan:
1. Nama file scene mengikuti nama produk aslinya — jangan di-rename sembarangan.
2. Setiap scene yang masuk `raw/` **wajib** dicatat di `docs/tabel_scene.md` (siapa yang unduh, kapan).
3. Baseline 100–200 titik/poligon: simpan di `baseline/` (GeoJSON), dokumentasikan cara pembuatannya di `docs/baseline.md`.
4. Tautan folder Drive tim: *[Drive](https://drive.google.com/drive/folders/19Z5n5ad4UBTn4HGypENv1LbVjq1oXRaw?usp=sharing)*
