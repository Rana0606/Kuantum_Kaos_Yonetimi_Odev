# Gerekli Modülleri İçe Aktarma
from abc import ABC, abstractmethod
import random
import sys

# --- 1. Arayüz (IKritik) ve Özel Hata (KuantumCokusuException) ---

class IKritik:
    """Interface Segregation Prensibine uygun IKritik Mixin Sınıfı."""
    # AcilDurumSogutmasi metodu, bu sınıfı miras alan tehlikeli nesneler tarafından uygulanmalıdır.
    def AcilDurumSogutmasi(self):
        # Bu metot somut sınıflar tarafından doldurulacaktır.
        raise NotImplementedError("Bu metot alt sınıflar tarafından uygulanmalıdır.")

class KuantumCokusuException(Exception):
    """Kural: Stabilite %0 altına düştüğünde fırlatılacak özel hata sınıfı (Custom Exception)."""
    def __init__(self, nesne_id):
        # Kural: Hatanın mesajında patlayan nesnenin ID'si yazmalıdır.
        super().__init__(f"Kritik Hata: Nesne ID '{nesne_id}' %0 stabilite altına düştü. Kuantum Çöküşü Başladı!")
        self.nesne_id = nesne_id

# --- 2. Temel Yapı (Abstract Class & Encapsulation) ---

class KuantumNesnesi(ABC): # ABC'den kalıtım alarak soyut sınıf olduğunu belirtiriz.
    """Kural: Tüm nesnelerin atası olan soyut (abstract) sınıf."""
    def __init__(self, id, stabilite, tehlike_seviyesi):
        # Kural: Kapsüllenmiş özel alan
        self._stabilite = 0.0 
        self.ID = id
        self.TehlikeSeviyesi = tehlike_seviyesi
        # Stabiliteyi başlatırken setter metodunu kullanır (Kapsülleme aktifleşir).
        self.Stabilite = stabilite 

    # Stabilite Getter (Okuma Metodu)
    @property
    def Stabilite(self):
        return self._stabilite

    # Stabilite Setter (Yazma Metodu) - Kapsülleme (Encapsulation) burada uygulanır.
    @Stabilite.setter
    def Stabilite(self, value):
        # Kural: 100'den büyük girilmesini engelle.
        if value > 100:
            self._stabilite = 100.0
        # Kural: 0'dan küçük girilmesini engelle. Eğer 0 veya altına düşerse, Kuantum Çöküşü gerçekleşir.
        elif value <= 0:
            self._stabilite = 0.0
            raise KuantumCokusuException(self.ID) # Kural: Hata fırlatılmalı.
        else:
            self._stabilite = value

    @abstractmethod
    def AnalizEt(self):
        # Kural: Soyut (abstract) metot. Alt sınıflar bunu kendine göre dolduracak.
        pass

    # Kural: Nesnenin ID'sini ve o anki stabilitesini string olarak döndüren metot.
    def DurumBilgisi(self):
        return f"[ID: {self.ID}] - Stabilite: {self.Stabilite:.2f}% - Tehlike Seviyesi: {self.TehlikeSeviyesi}"

# --- 3. Nesne Çeşitleri (Inheritance & Polymorphism) ---

class VeriPaketi(KuantumNesnesi):
    """Sıradan, güvenli veridir. IKritik değildir."""
    def AnalizEt(self):
        # Kural: Ekrana "Veri içeriği okundu." yazar.
        print(f"[INFO - {self.ID}] Veri içeriği okundu.") 
        # Kural: Stabilite 5 birim düşer.
        self.Stabilite -= 5 

class KaranlikMadde(KuantumNesnesi, IKritik):
    """Tehlikelidir. IKritik arayüzünü uygular."""
    def AnalizEt(self):
        print(f"[UYARI - {self.ID}] Karanlık Madde Analizi Yapılıyor...")
        # Kural: Stabilite 15 birim düşer.
        self.Stabilite -= 15

    def AcilDurumSogutmasi(self):
        # Kural: Stabiliteyi +50 artırır (Max 100 olacak şekilde).
        print(f"[SOĞUTMA - {self.ID}] Acil Durum Soğutması Yapıldı. (+50 Stabilite)")
        try:
            self.Stabilite += 50
        except KuantumCokusuException:
            pass # Soğutma çöküşe yol açmaz.

class AntiMadde(KuantumNesnesi, IKritik):
    """Çok Tehlikelidir. IKritik arayüzünü uygular. En Zorlu Olan."""
    def AnalizEt(self):
        # Kural: "Evrenin dokusu titriyor..." diye uyarı verir.
        print(f"[KRİTİK UYARI - {self.ID}] Evrenin dokusu titriyor...")
        # Kural: Stabilite 25 birim düşer.
        self.Stabilite -= 25

    def AcilDurumSogutmasi(self):
        # Kural: Stabiliteyi +50 artırır (Max 100 olacak şekilde).
        print(f"[SOĞUTMA - {self.ID}] Anti Madde Karantina Altına Alındı. (+50 Stabilite)")
        try:
            self.Stabilite += 50
        except KuantumCokusuException:
            pass

# --- 4. Oynanış Döngüsü (MAIN LOOP) ---

# Kural: Nesneleri saklamak için List<KuantumNesnesi> (Python listesi) kullanılır.
ENVANTER = []
NESNE_SAYACI = 1

def yeni_nesne_ekle():
    global NESNE_SAYACI
    tur_secimi = random.randint(1, 3) 
    yeni_id = f"QO-{NESNE_SAYACI:03d}"
    # Stabilite 50 ile 100 arası başlar
    baslangic_stabilite = random.randint(50, 100) 
    tehlike_seviyesi = random.randint(1, 10)
    NESNE_SAYACI += 1

    # Rastgele Nesne Üretimi
    if tur_secimi == 1:
        yeni_nesne = VeriPaketi(yeni_id, baslangic_stabilite, tehlike_seviyesi)
    elif tur_secimi == 2:
        yeni_nesne = KaranlikMadde(yeni_id, baslangic_stabilite, tehlike_seviyesi)
    else:
        yeni_nesne = AntiMadde(yeni_id, baslangic_stabilite, tehlike_seviyesi)

    ENVANTER.append(yeni_nesne)
    print(f"\n✅ Yeni Nesne Eklendi: {type(yeni_nesne).__name__} - {yeni_nesne.DurumBilgisi()}")

def envanteri_listele():
    print("\n--- ENVANTER DURUM RAPORU ---")
    if not ENVANTER:
        print("Ambarda henüz hiçbir nesne yok.")
        return

    # Kural: Polimorfizm - hepsinin DurumBilgisi() metodunu çağırın.
    for nesne in ENVANTER:
        print(nesne.DurumBilgisi())

def nesneyi_analiz_et():
    id = input("Analiz edilecek nesnenin ID'sini girin: ").upper()
    # Listede nesneyi bulma
    hedef_nesne = next((n for n in ENVANTER if n.ID == id), None)

    if hedef_nesne is None:
        print(f"Hata: ID '{id}' ile eşleşen nesne bulunamadı.")
        return

    print(f"\n👉 Nesne Analiz Ediliyor: {hedef_nesne.DurumBilgisi()}")
    # AnalizEt çağrılır. Bu işlem, stabilite 0'a düşerse KuantumCokusuException fırlatır.
    hedef_nesne.AnalizEt() 
    print(f"Analiz Tamamlandı. Yeni Durum: {hedef_nesne.DurumBilgisi()}")

def acil_durum_sogutmasi_yap():
    id = input("Soğutma yapılacak nesnenin ID'sini girin: ").upper()
    hedef_nesne = next((n for n in ENVANTER if n.ID == id), None)

    if hedef_nesne is None:
        print(f"Hata: ID '{id}' ile eşleşen nesne bulunamadı.")
        return

    # Kural: Type Checking (Tür Kontrolü) yapın. (isinstance() ile)
    if isinstance(hedef_nesne, IKritik):
        print(f"\n❄️ Soğutma Başlatılıyor: {hedef_nesne.DurumBilgisi()}")
        hedef_nesne.AcilDurumSogutmasi()
        print(f"Soğutma Tamamlandı. Yeni Durum: {hedef_nesne.DurumBilgisi()}")
    else:
        # Kural: Eğer sıradan bir VeriPaketi ise "Bu nesne soğutulamaz!" hatası verin.
        print(f"\n❌ HATA: Nesne ID '{id}' ({type(hedef_nesne).__name__}) kritik bir nesne değil. Bu nesne soğutulamaz!")

def menuyu_goster():
    # Kural: Program Main metodunda sonsuz bir döngü (while) içinde çalışmalıdır.
    print("\n=====================================")
    print("KUANTUM AMBARI KONTROL PANELİ")
    print("=====================================")
    print("1. Yeni Nesne Ekle")
    print("2. Tüm Envanteri Listele")
    print("3. Nesneyi Analiz Et")
    print("4. Acil Durum Soğutması Yap")
    print("5. Çıkış")
    print("=====================================")

def main_loop():
    print("KUANTUM VERİ AMBARI - HOŞ GELDİNİZ!")
    while True:
        try:
            menuyu_goster()
            secim = input("Seçiminiz: ").strip()

            if secim == '1': yeni_nesne_ekle()
            elif secim == '2': envanteri_listele()
            elif secim == '3': nesneyi_analiz_et()
            elif secim == '4': acil_durum_sogutmasi_yap()
            elif secim == '5':
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim.")

        # Kural: Eğer herhangi bir işlem sırasında KuantumCokusuException yakalanırsa (try-catch)...
        except KuantumCokusuException as ex:
            print("\n=======================================================")
            print(str(ex))
            # Kural: Ekrana büyük harflerle "SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR..." yazıp programı sonlandırın (Game Over).
            print("SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR...") 
            print("=======================================================")
            sys.exit() # Programı sonlandırır
        
        except Exception as ex:
            print(f"\nBeklenmeyen bir hata oluştu: {ex}")

        # Her tur sonunda devam etmek için enter beklenir.
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main_loop()