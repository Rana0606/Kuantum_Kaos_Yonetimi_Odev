// Main.java
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Main {

    private static final List<KuantumNesnesi> envanter = new ArrayList<>();
    private static int nesneSayaci = 1;
    private static final Random rnd = new Random();
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("KUANTUM VERİ AMBARI - HOŞ GELDİNİZ!");

        while (true) {
            try {
                menuyuGoster();
                String secim = scanner.nextLine();
                islemYap(secim);
            } 
            // Kural: KuantumCokusuException yakalanırsa Game Over.
            catch (KuantumCokusuException ex) {
                System.out.println("\n=======================================================");
                System.out.println(ex.getMessage());
                System.out.println("SİSTEM ÇÖKTÜ! TAHLİYE BAŞLATILIYOR..."); 
                System.out.println("=======================================================");
                return; // Programı sonlandırır
            }
            catch (Exception ex) {
                System.out.println("\nBeklenmeyen bir hata oluştu: " + ex.getMessage());
            }

            System.out.println("\nDevam etmek için Enter'a basın...");
            scanner.nextLine();
        }
    }

    private static void menuyuGoster() {
        System.out.println("\n=====================================");
        System.out.println("KUANTUM AMBARI KONTROL PANELİ");
        System.out.println("=====================================");
        System.out.println("1. Yeni Nesne Ekle (Rastgele Üretim)");
        System.out.println("2. Tüm Envanteri Listele (Durum Raporu)");
        System.out.println("3. Nesneyi Analiz Et (ID isteyerek)");
        System.out.println("4. Acil Durum Soğutması Yap (Sadece IKritik olanlar için!)");
        System.out.println("5. Çıkış");
        System.out.println("=====================================");
        System.out.print("Seçiminiz: ");
    }

    private static void islemYap(String secim) throws KuantumCokusuException {
        switch (secim) {
            case "1": yeniNesneEkle(); break;
            case "2": envanteriListele(); break;
            case "3": nesneyiAnalizEt(); break;
            case "4": acilDurumSogutmasiYap(); break;
            case "5": System.out.println("Çıkış yapılıyor."); System.exit(0); break;
            default: System.out.println("Geçersiz seçim."); break;
        }
    }

    // --- Yardımcı İşlem Metotları ---

    private static void yeniNesneEkle() {
        int turSecimi = rnd.nextInt(3) + 1; 
        String yeniID = String.format("QO-%03d", nesneSayaci++);
        double baslangicStabilite = rnd.nextInt(51) + 50; 

        KuantumNesnesi yeniNesne;
        int tehlikeSeviyesi = rnd.nextInt(10) + 1;

        switch (turSecimi) {
            case 1: yeniNesne = new VeriPaketi(yeniID, baslangicStabilite, tehlikeSeviyesi); break;
            case 2: yeniNesne = new KaranlikMadde(yeniID, baslangicStabilite, tehlikeSeviyesi); break;
            case 3: yeniNesne = new AntiMadde(yeniID, baslangicStabilite, tehlikeSeviyesi); break;
            default: return;
        }

        envanter.add(yeniNesne);
        System.out.println("\n✅ Yeni Nesne Eklendi: " + yeniNesne.getClass().getSimpleName() + " - " + yeniNesne.DurumBilgisi());
    }

    private static void envanteriListele() {
        System.out.println("\n--- ENVANTER DURUM RAPORU ---");
        if (envanter.isEmpty()) {
            System.out.println("Ambarda henüz hiçbir nesne yok.");
            return;
        }
        // Kural: Polimorfizm kullanın.
        for (KuantumNesnesi nesne : envanter) {
            System.out.println(nesne.DurumBilgisi());
        }
    }

    private static void nesneyiAnalizEt() throws KuantumCokusuException {
        System.out.print("Analiz edilecek nesnenin ID'sini girin: ");
        String id = scanner.nextLine().toUpperCase();

        KuantumNesnesi hedefNesne = envanter.stream()
            .filter(n -> n.ID.equals(id))
            .findFirst()
            .orElse(null);

        if (hedefNesne == null) {
            System.out.println("Hata: ID '" + id + "' ile eşleşen nesne bulunamadı.");
            return;
        }
        System.out.println("\n👉 Nesne Analiz Ediliyor: " + hedefNesne.DurumBilgisi());
        hedefNesne.AnalizEt();
        System.out.println("Analiz Tamamlandı. Yeni Durum: " + hedefNesne.DurumBilgisi());
    }

    private static void acilDurumSogutmasiYap() {
        System.out.print("Soğutma yapılacak nesnenin ID'sini girin: ");
        String id = scanner.nextLine().toUpperCase();

        KuantumNesnesi hedefNesne = envanter.stream()
            .filter(n -> n.ID.equals(id))
            .findFirst()
            .orElse(null);

        if (hedefNesne == null) {
            System.out.println("Hata: ID '" + id + "' ile eşleşen nesne bulunamadı.");
            return;
        }

        // Kural: Type Checking (Tür Kontrolü) yapın. (instanceof anahtar kelimesi)
        if (hedefNesne instanceof IKritik) {
            // Cast işlemi
            IKritik kritikNesne = (IKritik) hedefNesne; 
            
            System.out.println("\n❄️ Soğutma Başlatılıyor: " + hedefNesne.DurumBilgisi());
            kritikNesne.AcilDurumSogutmasi(); 
            System.out.println("Soğutma Tamamlandı. Yeni Durum: " + hedefNesne.DurumBilgisi());
        } else {
            // Kural: Eğer sıradan bir VeriPaketi ise hata verin.
            System.out.println("\n❌ HATA: Nesne ID '" + id + "' (" + hedefNesne.getClass().getSimpleName() + ") kritik bir nesne değil. Bu nesne soğutulamaz!");
        }
    }
}