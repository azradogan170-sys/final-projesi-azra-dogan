# SUV Araç Fiyat Tahmin Yapay Zekası Proje Raporu

## Proje Bağlantıları
* **Canlı Web Sitesi Linki:** https://final-projesi-azra-dogan-ixuwtzkyt6byqhjxxqc4xm.streamlit.app/
* **Proje Tanıtım ve Model Çalışma Videosu:** 

## Problem Tanımı ve Hedef Kullanıcı
İkinci el araç piyasasında, özellikle SUV model araçlarda fiyatlar marka, model yılı, kilometre ve piyasadaki talep durumu gibi birçok değişkene göre anlık olarak değişmektedir. Bu durum hem alıcılar hem de satıcılar için adil bir pazar fiyatı belirlemeyi zorlaştırmaktadır. 

Bu projenin hedef kitlesi; ikinci el SUV araç alım-satımı yapmak isteyen bireysel kullanıcılar ile piyasa analizi yapmak isteyen otomotiv meraklıları ve galeri sahipleridir.

## Çözümün Kısa Açıklaması ve Sistem İş Akışı
Projede bu probleme çözüm olarak makine öğrenmesi tabanlı bir akıllı veri ürünü geliştirilmiştir. İş akışı şu adımlardan oluşmaktadır:
1. İlk olarak Kaggle platformundan ham SUV araç pazar verileri alınmış ve temizlenmiştir.
2. Temizlenen bu veriler kullanılarak bir regresyon modeli eğitilmiştir.
3. Kullanıcıların bu modeli kolayca kullanabilmesi için arayüz tasarlanmıştır.
4. Son aşamada ise sistem internete yüklenerek herkesin erişebileceği canlı bir web sitesi haline getirilmiştir.

## Kullanılan Teknolojiler
Projenin geliştirilme sürecinde Python programlama dili kullanılmıştır. Verilerin analizi, temizlenmesi ve modelin eğitilmesi aşamalarında Pandas, NumPy, Scikit-Learn ve Joblib kütüphanelerinden yararlanılmıştır. Web sitesi arayüzü ve uygulamanın internette canlıya alınması için ise Streamlit platformu tercih edilmiştir. Kodlama ve eğitim süreçleri Google Colab ve GitHub üzerinde yürütülmüştür.

## Kurulum Adımları ve Kullanım Biçimi
Projeyi bilgisayarda yerel olarak çalıştırmak için öncelikle bu kod deposunun bilgisayara indirilmesi ve "requirements.txt" dosyasındaki gerekli kütüphanelerin yüklenmesi gerekmektedir. Ardından terminal üzerinden Streamlit komutu çalıştırılarak uygulama başlatılabilir.

Uygulamanın kullanımı oldukça basittir: Web sitesi açıldığında ekrandaki menülerden aracın markası, üretim yılı, kilometresi ve piyasadaki talep skoru seçilir. "Fiyat Tahmini Yap" butonuna basıldığında yapay zekâ modeli arka planda hesaplama yaparak Türkiye piyasasına uygun tahmini değeri ekrana yansıtır.

## Örnek Ekran Görüntüleri
<img width="1316" height="799" alt="image" src="https://github.com/user-attachments/assets/a2e3eeaa-78f5-440f-a697-2622fcd52f0b" />
<img width="1198" height="169" alt="image" src="https://github.com/user-attachments/assets/f5b5130c-5411-4754-9a58-7537db23f4a8" />


## Test Sonuçları ve Başarı Oranı
Modelin pazar verilerini öğrenme ve tahmin etme başarı oranı (R2 Skoru) %72.20 olarak ölçülmüştür. Canlı site üzerinde yapılan testlerde (örneğin 2022 model temiz bir Kia veya 2020 model düşük kilometreli bir Nissan girildiğinde) yapay zekanın Türkiye ikinci el SUV piyasası dinamiklerine oldukça yakın ve tutarlı fiyat tahminleri ürettiği doğrulanmıştır.

## Bilinen Sınırlılıklar ve Gelecekte Yapılabilecek Geliştirmeler
Modelimiz şu an için sadece veri setinde yer alan belirli SUV markaları üzerinden tahmin yürütebilmektedir. Ayrıca araçların fiyatını doğrudan etkileyen kaza durumu, boyalı parça sayısı, hasar kaydı veya donanım paketi gibi detaylı bilgiler ham veri setinde bulunmadığı için modele dahil edilememiştir. 

Gelecekte bu tarz hasar ve donanım bilgileri de veri setine eklenerek modelin tahmin gücü artırılabilir. Ayrıca Lineer Regresyon algoritması yerine daha gelişmiş yapay zekâ algoritmaları denenerek başarı oranı daha da yukarı taşınabilir.

## Yapay Zekâ Araçlarının Kullanıldığı Aşamalar
Projenin Google Colab ortamındaki veri ön işleme süreçlerinde, Streamlit arayüz kodlarının yazımında ve uygulamayı canlı ortama aktarırken karşılaşılan kütüphane uyuşmazlığı sorunlarının giderilmesinde, yapay zekâ tabanlı kodlama asistanlarından teknik destek ve kod düzeltme yardımı alınmıştır.
