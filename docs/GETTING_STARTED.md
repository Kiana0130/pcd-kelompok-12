# GETTING STARTED — Panduan Kerja Tim (Git & GitHub)

Panduan buat kita bertiga. Baca sekali, praktik terus jadi hafal. 🙌

## 0. Setup awal (sekali saja per orang)

```bash
# 1. Clone repo
git clone https://github.com/<username-kita>/<nama-repo>.git
cd <nama-repo>

# 2. Setting identitas git (sekali saja)
git config user.name "Nama Kamu"
git config user.email "emailkamu@..."

# 3. Bikin virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 1. Konsep kilat

- **Repo** = folder proyek + seluruh riwayat perubahannya.
- **Commit** = "save point" — snapshot perubahan beserta pesannya.
- **Branch** = jalur kerja terpisah. `main` = versi resmi. Kita kerja di branch masing-masing supaya tidak saling tabrakan.
- **Push** = mengirim commit dari laptop ke GitHub.
- **Pull Request (PR)** = permintaan "tolong gabungkan branch-ku ke main" — tempat teman mereview sebelum kode masuk `main`.

## 2. Alur kerja sehari-hari (hapal urutan ini)

```bash
# 1. Mulai kerja: pastikan main terbaru
git checkout main
git pull origin main

# 2. Bikin branch untuk tugas yang mau dikerjakan
git checkout -b feat/segmentasi-mndwi    # nama bebas: feat/..., fix/..., docs/...

# 3. Kerja... edit file, bikin notebook, dsb.

# 4. Cek apa yang berubah
git status
git diff

# 5. Simpan sebagai commit (boleh beberapa kali)
git add path/ke/file
git commit -m "tambah threshold Otsu untuk MNDWI"

# 6. Kirim ke GitHub
git push -u origin feat/segmentasi-mndwi

# 7. Buka GitHub → tombol "Compare & pull request" → isi deskripsi → Create PR
# 8. Minta satu teman review. Setelah di-approve → Merge di GitHub.
# 9. Bersihkan branch lokal:
git checkout main && git pull origin main
git branch -d feat/segmentasi-mndwi
```

## 3. Aturan tim (disepakati bareng)

1. **Jangan pernah commit langsung ke `main`** — selalu lewat branch + PR.
2. **Satu branch = satu tugas kecil** (mis. "fungsi crop AOI", bukan "semua preprocessing").
3. `git pull origin main` **setiap mulai kerja**, biar tidak ketinggalan.
4. File citra (`*.tif`, dll.) **tidak boleh di-commit** — masuk Drive tim. `.gitignore` sudah menjaga, jangan pakai `git add -f`.
5. Commit message bahasa Indonesia tidak masalah, format: `tambah/perbaiki/hapus + apa`.
6. Konflik merge itu normal — selesaikan bareng di VS Code (ada tombol Accept Current/Incoming), jangan panik, jangan `git reset --hard` diam-diam.

## 4. Pakai AI agent? Wajib begini

Sebelum minta bantuan AI apa pun (Claude, Copilot, ChatGPT, Cursor, Hermes...):

1. **Arahkan AI ke `AGENTS.md`** — misal di awal chat: *"Baca AGENTS.md di root repo ini dan patuhi semua aturannya sebelum mengerjakan apa pun."* Di Claude Code/Cursor, file `AGENTS.md` di root biasanya otomatis terbaca.
2. Jangan biarkan AI mengubah: AOI, metode threshold, struktur pipeline, tabel scene.
3. Jangan biarkan AI mengarang angka hasil — semua angka harus dari eksekusi kode nyata.
4. Review setiap perubahan AI sebelum di-commit. Kamu yang bertanggung jawab atas kode yang masuk PR, bukan AI-nya.

## 5. Kalau ada masalah

| Masalah | Solusi |
|---|---|
| `git push` ditolak | `git pull origin <branch>` dulu, selesaikan konflik, push lagi |
| Salah commit file besar | **jangan push** — `git reset HEAD~1` lalu perbaiki `.gitignore` |
| Sudah terlanjur push file besar | Kabari tim, bersihkan bareng (filter-repo), jangan diam-diam |
| Bingung kondisi repo | `git status` + `git log --oneline -10` lalu screenshot, diskusikan |
