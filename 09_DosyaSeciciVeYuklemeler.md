# Dosya Seçici ve Yüklemeler

[Dosya seçici](https://flet.dev/docs/controls/filepicker/) kontrolü, dosyaları ve dizinleri seçmek için yerel bir işletim sistemi iletişim kutusu açar.

Tüm platformlarda çalışır: Web, macOS, Window, Linux, iOS ve Android.

![](https://flet.dev/img/docs/controls/file-picker/file-picker-all-modes-demo.png)

[Yukarıdaki demonun kaynak kodunu](https://github.com/flet-dev/examples/blob/main/python/controls/file-picker/file-picker-all-modes.py) kontrol edin.

Dosya seçici, üç iletişim kutusunun açılmasına izin verir:

* **Dosyaları seç** - bir veya daha fazla, herhangi bir dosya veya yalnızca belirli türler.

* **Dosyayı kaydet** - dizini ve dosya adını seçin.

* **Dizini al** - dizini seçin.

Flet uygulamasını bir tarayıcıda çalıştırırken yalnızca "Dosyaları seç" seçeneği kullanılabilir ve yalnızca yüklemeler için kullanılır, çünkü seçili bir dosyanın tam yolunu döndürmez.

Dosya seçicinin gerçekten parladığı yer masaüstüdür! Üç iletişim kutusu da seçilen dosya ve dizinlerin tam yollarını döndürür - kullanıcılarınız için harika bir yardım!



# Uygulamanızda dosya seçiciyi kullanma


