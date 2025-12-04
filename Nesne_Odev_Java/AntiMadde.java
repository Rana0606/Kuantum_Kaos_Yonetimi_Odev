// AntiMadde.java
public class AntiMadde extends KuantumNesnesi implements IKritik {
    public AntiMadde(String id, double baslangicStabilite, int tehlikeSeviyesi) {
        super(id, baslangicStabilite, tehlikeSeviyesi);
    }
    @Override
    public void AnalizEt() throws KuantumCokusuException {
        System.out.println("[KRİTİK UYARI - " + ID + "] Evrenin dokusu titriyor..."); 
        // Stabilite 25 birim düşer.
        setStabilite(getStabilite() - 25.0);
    }
    @Override
    public void AcilDurumSogutmasi() {
        System.out.println("[SOĞUTMA - " + ID + "] Anti Madde Karantina Altına Alındı. (+50 Stabilite)");
        try {
            setStabilite(getStabilite() + 50.0);
        } catch (KuantumCokusuException ignored) {}
    }
}