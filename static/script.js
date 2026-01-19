// Logika Kalkulator

let first = null;
let operation = null;

function append(val) {
    document.getElementById("display").value += val;
}

function clearDisplay() {
    document.getElementById("display").value = "";
    first = null;
    operation = null;
}

// Untuk operasi 2 angka (+, -, *, /)
function setOp(op) {
    first = document.getElementById("display").value;
    operation = op;
    document.getElementById("display").value = "";
}

// Dipanggil saat tombol "=" ditekan
function calculate() {
    let second = document.getElementById("display").value;
    // Kirim operasi yang disimpan, angka pertama, dan angka kedua (layar sekarang)
    send(operation, first, second);
}

// LOGIKA UTAMA (YANG DIPERBAIKI)
function send(op, a = null, b = null) {
    
    // PERBAIKAN: Deteksi tombol Scientific
    // Jika 'a' kosong saat fungsi dipanggil, berarti ini tombol scientific (sin, cos, dll)
    // Maka ambil nilai 'a' langsung dari layar calculator.
    if (a === null) {
        a = document.getElementById("display").value;
        b = 0; // Scientific biasanya cuma butuh 1 angka
    }

    // Khusus PI, tidak butuh input dari layar
    if (op === 'pi') {
        a = 0; 
    }
    
    // Validasi sederhana agar tidak kirim data kosong
    if (a === "" && op !== 'pi') return;

    fetch("/calculate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            operation: op, 
            a: a, 
            b: b
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("display").value = data.result;
        // Reset state setelah hasil keluar
        first = null;
        operation = null;
    })
    .catch(err => {
        console.error("Error:", err);
        document.getElementById("display").value = "Error";
    });
}
