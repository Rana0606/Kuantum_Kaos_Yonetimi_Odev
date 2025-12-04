// KuantumNesnesi.cs
using System;

// Tüm nesnelerin atası olan soyut (abstract) bir sınıf.
public abstract class KuantumNesnesi
{
    // Kapsüllenmiş özel alan (backing field)
    private double _stabilite;
    
    // Özellikler (CS1014 hatasını düzeltir)
    public string ID { get; protected set; } 
    public int TehlikeSeviyesi { get; protected set; } 

    // Stabilite Özelliği (Kapsülleme)
    public double Stabilite
    {
        get { return _stabilite; }
        protected set
        {
            // Kapsülleme: 100'den büyük veya 0'dan küçük girilmesini engeller.
            if (value > 100)
            {
                _stabilite = 100.0;
            }
            else if (value <= 0) // Kuantum Çöküşü kontrolü
            {
                _stabilite = 0.0;
                // Stabilite 0 veya altına düştüğünde hata fırlatılır.
                throw new KuantumCokusuException(ID); 
            }
            else
            {
                _stabilite = value;
            }
        }
    }

    // Kurucu Metot (Constructor)
    public KuantumNesnesi(string id, double baslangicStabilite, int tehlikeSeviyesi)
    {
        this.ID = id;
        this.TehlikeSeviyesi = tehlikeSeviyesi;
        // Kapsülleme aktifleşir.
        this.Stabilite = baslangicStabilite; 
    }

    // Soyut (abstract) metot.
    public abstract void AnalizEt();

    // Durum bilgisini döndüren metot.
    public string DurumBilgisi()
    {
        return $"[ID: {ID}] - Stabilite: {Stabilite:F2}% - Tehlike Seviyesi: {TehlikeSeviyesi}";
    }
}