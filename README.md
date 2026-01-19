# Scientific-Calculator

Aplikasi **Scientific Calculator** berbasis web yang dibuat menggunakan **Python Flask**.  
Aplikasi ini meniru fungsi kalkulator scientific seperti pada kalkulator fisik, dengan tampilan interaktif dan backend Python yang aman (tanpa `eval()`).

---

## Fitur
### Operasi Dasar
- Penjumlahan (+)
- Pengurangan (−)
- Perkalian (×)
- Pembagian (÷)

### Operasi Scientific
- Pangkat (xʸ)
- Akar kuadrat (√x)
- Trigonometri: sin, cos, tan
- Logaritma: log, ln
- Konstanta π (pi)
- Clear display (C)

---

## Struktur Proyek
```text
scientific-calculator/
│
├── app.py # Aplikasi utama Flask (backend)
├── math_ops.py # Modul operasi matematika & scientific
│
├── templates/
│ └── calculator.html # Tampilan kalkulator (HTML)
│
└── static/
├── style.css # Styling tampilan kalkulator
└── script.js # Logika interaksi (JavaScript)
```

---

## Teknologi yang Digunakan
- Python 3
- Flask
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## Cara Menjalankan Aplikasi
1. Clone Repository
```bash
git clone https://github.com/USERNAME/scientific-calculator.git
cd scientific-calculator
```
2. Install Dependency
```bash
pip install flask
```
3. Jalankan Aplikasi
```bash
python app.py
```
4. Buka di Browser
[Local Server](http://127.0.0.1:5000)
