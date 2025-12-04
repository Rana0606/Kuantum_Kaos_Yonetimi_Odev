public class KuantumCokusuException extends Exception {
    public KuantumCokusuException(String nesneId) {
        super("Kritik Hata: Nesne ID '" + nesneId + "' %0 stabilite altına düştü. Kuantum Çöküşü Başladı!");
    }
}