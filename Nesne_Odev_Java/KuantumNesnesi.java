// KuantumNesnesi.java
public abstract class KuantumNesnesi {
    
    // Kapsüllenmiş özel alan (private field)
    private double stabilite;
    
    // ID ve TehlikeSeviyesi sadece Kurucu Metot (Constructor) ile atanır.
    protected final String ID; 
    protected final int tehlikeSeviyesi; 

    // Constructor
    public KuantumNesnesi(String id, double baslangicStabilite, int tehlikeSeviyesi) {
        this.ID = id;
        this.tehlikeSeviyesi = tehlikeSeviyesi;
        try {
            // Başlangıç değerini atarken setStabilite kullanılır.
            this.setStabilite(baslangicStabilite);
        } catch (KuantumCokusuException ignored) {
            // Başlangıçta çöküş beklenmez.
        }
    }

    // Stabiliteyi okumak için Getter
    public double getStabilite() {
        return stabilite;
    }

    // Stabiliteyi ayarlamak için Setter (Kapsülleme)
    protected void setStabilite(double yeniStabilite) throws KuantumCokusuException {
        if (yeniStabilite > 100.0) {
            this.stabilite = 100.0;
        } else if (yeniStabilite <= 0.0) {
            this.stabilite = 0.0;
            // Kuantum Çöküşü (Quantum Collapse) gerçekleşirse hata fırlatılır.
            throw new KuantumCokusuException(this.ID); 
        } else {
            this.stabilite = yeniStabilite;
        }
    }

    // Soyut Metot: Alt sınıflar bunu zorunlu olarak uygulamalıdır.
    public abstract void AnalizEt() throws KuantumCokusuException;

    public String DurumBilgisi() {
        return String.format("[ID: %s] - Stabilite: %.2f%% - Tehlike Seviyesi: %d", 
            ID, stabilite, tehlikeSeviyesi);
    }
}