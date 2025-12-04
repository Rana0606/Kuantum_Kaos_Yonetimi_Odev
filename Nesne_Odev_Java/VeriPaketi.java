// VeriPaketi.java
public class VeriPaketi extends KuantumNesnesi {
    public VeriPaketi(String id, double baslangicStabilite, int tehlikeSeviyesi) {
        super(id, baslangicStabilite, tehlikeSeviyesi);
    }
    @Override
    public void AnalizEt() throws KuantumCokusuException {
        System.out.println("[INFO - " + ID + "] Veri içeriği okundu.");
        // Stabilite sadece 5 birim düşer.
        setStabilite(getStabilite() - 5.0); 
    }
}