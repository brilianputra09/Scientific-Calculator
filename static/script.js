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

function setOp(op) {
    first = document.getElementById("display").value;
    operation = op;
    document.getElementById("display").value = "";
}

function calculate() {
    let second = document.getElementById("display").value;
    send(operation, first, second);
}

function send(op, a=null, b=null) {
    fetch("/calculate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({operation: op, a: a, b: b})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("display").value = data.result;
    });
}
