function randomIntFromInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

const tongLS=2000000000;
let lsHienTai=0
const soHang=[];

while (lsHienTai < tongLS) {
    const soRd=randomIntFromInterval(0, 999999);
    if ((lsHienTai + soRd)<=tongLS) {
        lsHienTai+=soRd;
        soHang.push(soRd)
    }
}

for (let i=0; i<=10000; i++) {
    soHang.push(randomIntFromInterval(0, 999999));
}

copy(soHang.join(" "))
console.log(soHang.length)