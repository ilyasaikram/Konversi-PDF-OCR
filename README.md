# Konverter PDF OCR

Skrip Python untuk mengonversi file PDF hasil pindai (scanned) menjadi PDF yang dapat dicari (searchable) menggunakan Pengenalan Karakter Optik (OCR) dengan dukungan multi-bahasa.

## Fitur

- **Dukungan OCR Multi-bahasa**: Dukungan default untuk bahasa Inggris (`eng`) dan Indonesia (`ind`)
- **Mode OCR Fleksibel**: Tiga mode berbeda untuk menangani teks yang sudah ada dalam PDF
- **Mempertahankan Kualitas Asli**: Tidak ada kompresi lossy yang diterapkan pada file output
- **Antarmuka Baris Perintah**: Mudah diintegrasikan ke dalam alur kerja dan skrip otomasi

## Prasyarat

- Python 3.7 atau lebih tinggi
- Mesin OCR Tesseract terinstal di sistem Anda
- Pustaka Python ocrmypdf

## Instalasi

### 1. Instal Dependensi Sistem

Pertama, instal Tesseract OCR pada sistem Anda:

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-eng    # Paket bahasa Inggris
sudo apt-get install tesseract-ocr-ind    # Paket bahasa Indonesia
```

**macOS (menggunakan Homebrew):**
```bash
brew install tesseract
brew install tesseract-lang    # Untuk paket bahasa tambahan
```

**Windows:**
Unduh dan instal Tesseract dari [rilis GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

### 2. Instal Dependensi Python

```bash
pip install ocrmypdf
```

Skrip `OCR.py` akan berfungsi secara otomatis setelah `ocrmypdf` terinstal.

## Penggunaan

### Struktur Perintah Dasar

```bash
python OCR.py -i input.pdf -o output.pdf
```

### Argumen Baris Perintah

| Argumen | Diperlukan | Deskripsi | Default |
|---------|------------|-----------|---------|
| `-i`, `--i` | Ya | Jalur ke file PDF input | - |
| `-o`, `--o` | Ya | Jalur ke file PDF output | - |
| `--lang` | Tidak | Bahasa untuk OCR (gunakan `+` untuk multiple) | `eng+ind` |
| `--mode` | Tidak | Mode penanganan OCR: `redo`, `force`, atau `skip` | `redo` |

### Penjelasan Mode OCR

1. **`redo` (default)**: Melakukan ulang OCR pada halaman yang sudah memiliki teks
2. **`force`**: Memaksa OCR dengan merasterisasi semua halaman (berguna untuk pindaian berkualitas rendah)
3. **`skip`**: Melewati halaman yang sudah mengandung teks (untuk PDF yang sebagian dapat dicari)

### Kode Bahasa

Parameter `--lang` menerima kode bahasa standar Tesseract:

- `eng` - Inggris
- `ind` - Indonesia
- `eng+ind` - Inggris dan Indonesia (default)
- `fra` - Perancis
- `deu` - Jerman
- `spa` - Spanyol
- `jpn` - Jepang
- dll. (lihat dokumentasi Tesseract untuk daftar lengkap)

## Contoh

### Contoh 1: Konversi Dasar
```bash
python OCR.py -i dokumen_scan.pdf -o dokumen_searchable.pdf
```

### Contoh 2: Menentukan Bahasa
```bash
python OCR.py -i dokumen_perancis.pdf -o hasil_perancis.pdf --lang fra
```

### Contoh 3: Paksa OCR di Semua Halaman
```bash
python OCR.py -i kualitas_rendah.pdf -o diperbaiki.pdf --mode force
```

### Contoh 4: Lewati Halaman dengan Teks yang Sudah Ada
```bash
python OCR.py -i sebagian_searchable.pdf -o fully_searchable.pdf --mode skip
```

### Contoh 5: Beberapa Bahasa
```bash
python OCR.py -i multilingual.pdf -o output.pdf --lang eng+ind+spa
```

## Catatan Kualitas Output

- Skrip menggunakan `optimize=0` untuk mempertahankan kualitas gambar asli
- Tidak ada deskewing atau pembersihan yang diterapkan secara default (membutuhkan instalasi `unpaper`)
- Untuk hasil terbaik dengan pindaian miring atau kotor, instal `unpaper`:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install unpaper
  
  # Perbarui opsi skrip:
  # Ubah deskew=False dan clean=False menjadi True dalam skrip
  ```

## Pemecahan Masalah

### Masalah Umum

1. **Error "Tesseract not found"**: Pastikan Tesseract terinstal dan ada dalam PATH sistem Anda
2. **Akurasi OCR buruk**: Coba gunakan `--mode force` atau pra-proses gambar untuk kontras yang lebih baik
3. **Dukungan bahasa tidak ada**: Instal paket bahasa Tesseract yang diperlukan
4. **Ukuran file besar**: Output mempertahankan kualitas asli; gunakan alat optimasi PDF terpisah jika diperlukan

### Menguji Hasil OCR

Skrip merekomendasikan pengujian output di Adobe Acrobat untuk pengalaman terbaik melihat lapisan teks yang dapat dicari.

## Integrasi

Skrip ini dapat diintegrasikan ke dalam alur kerja yang lebih besar:

```bash
# Contoh pemrosesan batch
for file in *.pdf; do
    python OCR.py -i "$file" -o "searchable_${file}"
done
```

## Lisensi

Skrip ini disediakan apa adanya. Pustaka `ocrmypdf` dilisensikan di bawah lisensi MPL-2.0. Pastikan Anda mematuhi semua lisensi yang relevan saat menggunakan alat ini.

## Ucapan Terima Kasih

- Dibangun dengan [ocrmypdf](https://github.com/ocrmypdf/OCRmyPDF)
- Menggunakan [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Mendukung berbagai bahasa melalui paket bahasa Tesseract

## Dukungan

Untuk masalah akurasi OCR, lihat [dokumentasi Tesseract](https://tesseract-ocr.github.io/tessdoc/).
Untuk masalah spesifik skrip, pastikan semua dependensi terinstal dengan benar dan jalur ditentukan dengan tepat.
