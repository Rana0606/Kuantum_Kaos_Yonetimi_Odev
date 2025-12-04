// Gerekli Modülleri İçe Aktarma (Node.js için)
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// --- 1. Özel Hata (Custom Exception) ---

class KuantumCokusuException extends Error {
    constructor(nesneId) {
        // Kural: Mesajda patlayan nesnenin ID'si yazmalıdır.
        super(`Kritik Hata: Nesne ID '${nesneId}' %0 stabilite altına düştü. Kuantum Çöküşü Başladı!`);
        this.name = 'KuantumCokusuException';
        this.nesneId = nesneId;
    }
}

// --- 2. Temel Yapı (Abstract Class & Encapsulation) ---

class KuantumNesnesi {
    constructor(id, stabilite, tehlikeSeviyesi) {
        this._stabilite = 0.0; // Kapsüllenmiş özel alan
        this.ID = id;
        this.TehlikeSeviyesi = tehlikeSeviyesi;
        // Setter metodunu kullanır (Kapsülleme aktifleşir).
        this.stabilite = stabilite; 

        // Javascript'te Abstract Sınıf Kontrolü
        if (new.target === KuantumNesnesi) {
            throw new TypeError("KuantumNesnesi soyut bir sınıftır ve doğrudan örneklendirilemez.");
        }
    }

    // Stabilite Getter (Okuma Metodu)
    get stabilite() {
        return this._stabilite;
    }

    // Stabilite Setter (Yazma Metodu) - Kapsülleme (Encapsulation) burada uygulanır.
    set stabilite(value) {
        // Kural: 100'den büyük veya 0'dan küçük girilmesini engelle.
        if (value > 100) {
            this._stabilite = 100.0;
        } else if (value <= 0) {
            this._stabilite = 0.0;
            // Kural: Stabilite 0 veya altına düştüğünde hata fırlatılır.
            throw new KuantumCokusuException(this.ID);
        } else {
            this._stabilite = value;
        }
    }

    AnalizEt() {
        // Kural: Alt sınıflar AnalizEt metodunu uygulamalıdır (Abstract).
        throw new Error("AnalizEt metodu alt sınıflarda uygulanmalıdır."); 
    }

    // Kural: Nesnenin ID'sini ve o anki stabilitesini döndüren metot.
    DurumBilgisi() {
        return `[ID: ${this.ID}] - Stabilite: ${this.stabilite.toFixed(2)}% - Tehlike Seviyesi: ${this.TehlikeSeviyesi}`;
    }
}

// Javascript'te Arayüz (Interface) simülasyonu (Marker olarak kullanılır)
function IKritik() {}


// --- 3. Nesne Çeşitleri (Inheritance & Polymorphism) ---

class VeriPaketi extends KuantumNesnesi {
    AnalizEt() {
        console.log(`[INFO - ${this.ID}] Veri içeriği okundu.`); //
        // Kural: Stabilite 5 birim düşer.
        this.stabilite -= 5; 
    }
}

class KaranlikMadde extends KuantumNesnesi {
    constructor(id, stabilite, tehlikeSeviyesi) {
        super(id, stabilite, tehlikeSeviyesi);
        // IKritik uygular (Prototip / Mixin ekleme)
        Object.assign(this, IKritik.prototype); 
    }

    AnalizEt() {
        console.log(`[UYARI - ${this.ID}] Karanlık Madde Analizi Yapılıyor...`);
        // Kural: Stabilite 15 birim düşer.
        this.stabilite -= 15;
    }

    AcilDurumSogutmasi() {
        console.log(`[SOĞUTMA - ${this.ID}] Acil Durum Soğutması Yapıldı. (+50 Stabilite)`);
        try {
            this.stabilite += 50; // Kural: Stabiliteyi +50 artırır (Max 100).
        } catch (e) {
        }
    }
}

class AntiMadde extends KuantumNesnesi {
    constructor(id, stabilite, tehlikeSeviyesi) {
        super(id, stabilite, tehlikeSeviyesi);
        // IKritik uygular
        Object.assign(this, IKritik.prototype);
    }

    AnalizEt() {
        console.log(`[KRİTİK UYARI - ${this.ID}] Evrenin dokusu titriyor...`); //
        // Kural: Stabilite 25 birim düşer.
        this.stabilite -= 25; 
    }

    AcilDurumSogutmasi() {
        console.log(`[SOĞUTMA - ${this.ID}] Anti Madde Karantina Altına Alındı. (+50 Stabilite)`);
        try {
            this.stabilite += 50; // Kural: Stabiliteyi +50 artırır (Max 100).
        } catch (e) {
        }
    }
}

// --- 4. Oynanış Döngüsü (MAIN LOOP) ---

const ENVANTER = []; // Kural: List<KuantumNesnesi>
let NESNE_SAYACI = 1;

function yeniNesneEkle() {
    const turSecimi = Math.floor(Math.random() * 3) + 1;
    // ID formatı QO-XXX (3 haneli)
    const yeniID = `QO-${NESNE_SAYACI++}`.padStart(6, '0'); 
    const baslangicStabilite = Math.floor(Math.random() * 51) + 50;
    const tehlikeSeviyesi = Math.floor(Math.random() * 10) + 1;

    let yeniNesne;

    if (turSecimi === 1) {
        yeniNesne = new VeriPaketi(yeniID, baslangicStabilite, tehlikeSeviyesi);
    } else if (turSecimi === 2) {
        yeniNesne = new KaranlikMadde(yeniID, baslangicStabilite, tehlikeSeviyesi);
    } else {
        yeniNesne = new AntiMadde(yeniID, baslangicStabilite, tehlikeSeviyesi);
    }

    ENVANTER.push(yeniNesne);
    console.log(`\n✅ Yeni Nesne Eklendi: ${yeniNesne.constructor.name} - ${yeniNesne.DurumBilgisi()}`);
}

async function envanteriListele() {
    console.log("\n--- ENVANTER DURUM RAPORU ---");
    if (ENVANTER.length === 0) {
        console.log("Ambarda henüz hiçbir nesne yok.");
        return;
    }

    // Kural: Polimorfizm - hepsinin DurumBilgisi() metodunu çağırın.
    ENVANTER.forEach(nesne => {
        console.log(nesne.DurumBilgisi());
    });
}

async function nesneyiAnalizEt() {
    // Kullanıcıdan ID isteme
    const id = await new Promise(resolve => rl.question("Analiz edilecek nesnenin ID'sini girin: ", resolve));
    const hedefNesne = ENVANTER.find(n => n.ID === id.toUpperCase());

    if (!hedefNesne) {
        console.log(`Hata: ID '${id}' ile eşleşen nesne bulunamadı.`);
        return;
    }

    console.log(`\n👉 Nesne Analiz Ediliyor: ${hedefNesne.DurumBilgisi()}`);
    hedefNesne.AnalizEt(); 
    console.log(`Analiz Tamamlandı. Yeni Durum: ${hedefNesne.DurumBilgisi()}`);
}

async function acilDurumSogutmasiYap() {
    const id = await new Promise(resolve => rl.question("Soğutma yapılacak nesnenin ID'sini girin: ", resolve));
    const hedefNesne = ENVANTER.find(n => n.ID === id.toUpperCase());

    if (!hedefNesne) {
        console.log(`Hata: ID '${id}' ile eşleşen nesne bulunamadı.`);
        return;
    }

    // Kural: Type Checking (Tür Kontrolü) yapın. ('instanceof' ile)
    if (hedefNesne instanceof KaranlikMadde || hedefNesne instanceof AntiMadde) {
        console.log(`\n❄️ Soğutma Başlatılıyor: ${hedefNesne.DurumBilgisi()}`);
        hedefNesne.AcilDurumSogutmasi();
        console.log(`Soğutma Tamamlandı. Yeni Durum: ${hedefNesne.DurumBilgisi()}`);
    } else {
        // Kural: Eğer sıradan bir VeriPaketi ise "Bu nesne soğutulamaz!" hatası verin.
        console.log(`\n❌ HATA: Nesne ID '${id}' (${hedefNesne.constructor.name}) kritik bir nesne değil. Bu nesne soğutulamaz!`);
    }
}

async function mainLoop() {
    console.log("KUANTUM VERİ AMBARI - HOŞ GELDİNİZ!");

    while (true) { // Kural: Sonsuz döngü
        try {
            console.log("\n=====================================");
            console.log("KUANTUM AMBARI KONTROL PANELİ");
            console.log("=====================================");
            console.log("1. Yeni Nesne Ekle");
            console.log("2. Tüm Envanteri Listele");
            console.log("3. Nesneyi Analiz Et");
            console.log("4. Acil Durum Soğutması Yap");
            console.log("5. Çıkış");
            console.log("=====================================");

            const secim = await new Promise(resolve => rl.question("Seçiminiz: ", resolve));

            switch (secim.trim()) {
                case '1': await yeniNesneEkle(); break;
                case '2': await envanteriListele(); break;
                case '3': await nesneyiAnalizEt(); break;
                case '4': await acilDurumSogutmasiYap(); break;
                case '5':
                    console.log("Çıkış yapılıyor...");
                    rl.close();
                    return;
                default:
                    console.log("Geçersiz seçim.");
            }

        } catch (error) {
            // Kural: KuantumCokusuException yakalanırsa Game Over.
            if (error instanceof KuantumCokusuException) {
                console.log("\n=======================================================");
                console.error(error.message);
                console.error("SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR..."); 
                console.log("=======================================================");
                rl.close();
                return; 
            } else {
                console.error(`\nBeklenmeyen bir hata oluştu: ${error.message}`);
            }
        }

        await new Promise(resolve => rl.question("\nDevam etmek için Enter'a basın...", resolve));
    }
}

mainLoop();