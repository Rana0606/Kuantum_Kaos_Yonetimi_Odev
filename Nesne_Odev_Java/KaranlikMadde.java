// KaranlikMadde.java
public class KaranlikMadde extends KuantumNesnesi implements IKritik {
    public KaranlikMadde(String id, double baslangicStabilite, int tehlikeSeviyesi) {
        super(id, baslangicStabilite, tehlikeSeviyesi);
    }
    @Override
    public void AnalizEt() throws KuantumCokusuException {
        System.out.println("[UYARI - " + ID + "] Karanlık Madde Analizi Yapılıyor...");
        // Stabilite 15 birim düşer.
        setStabilite(getStabilite() - 15.0);
    }
    @Override
    public void AcilDurumSogutmasi() {
        System.out.println("[SOĞUTMA - " + ID + "] Acil Durum Soğutması Yapıldı. (+50 Stabilite)");
        try {
            // Stabiliteyi 50 artır. Max 100 kuralı setStabilite içinde işler.
            setStabilite(getStabilite() + 50.0);
        } catch (KuantumCokusuException ignored) {}
    }
}