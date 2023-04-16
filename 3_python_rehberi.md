# Python Rehberi

# Python'da Flet uygulamaları oluşturma

Bir **Flet** uygulaması yazmak için front-end gurusu olmanız gerekmez, ancak temel 
**Python** bilgisine ve Nesne Yönelimli Programlama (OOP) bilgisine sahip olmanız önerilir.

Bu kılavuzda (rehberde), bir Flet uygulamasının yapısını inceleyeceğiz, **Flet** **kontrollerini** kullanarak veri çıktısını almayı, bir kullanıcıdan veri istemeyi ve temel sayfa düzenleri oluşturmayı öğreneceğiz. 
Kullanıcılarınıza hazır bir uygulama sunmak için bazı paketleme ve dağıtım seçeneklerini de ele alacağız.

## Flet modülünü yükleme

**Flet**, <u>Python 3.7 veya üst sürümünü</u> gerektirir. Flet ile arabirim oluşturmak için önce **flet** modülünü kurmanız gerekir:

```
pip install flet
```

> Flet modülünü yükseltmek için aşağıdaki kodu çalıştırmalısınız:
> 
> ```
> pip install flet --upgrade
> ```

Flet ön sürümünü (pre-release) yüklemek için (ileri düzey kullanıcılar için) aşağıdaki kodu çalıştırın:

```
pip install flet --pre
```

> Dikkat!
> 
> Ön sürüm (pre-release) yapılarını, bir sanal ortama yüklemenizi öneririz.

### Linux

**Flet** uygulamalarını Linux ve **WSL**'de çalıştırmak için [GStreamer](https://gstreamer.freedesktop.org/) kitaplıklarının kurulu olması gerekir. Büyük olasılıkla zaten sisteminizde vardır, ancak Flet uygulamasını çalıştırırken `error while loading shared libraries: libgstapp-1.0.so.0: cannot open shared object file: No such file or directory` şeklinde hata alıyorsanız, **GStreamer**'ı yüklemeniz gerekir .

GStreamer'ı Ubuntu/Debian'a yüklemek için aşağıdaki komutları çalıştırın:

```
sudo apt-get update
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

GStreamer'ı, diğer Linux dağıtımlarına yüklemek için [bu kılavuza](https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c) göz atın.

### WSL

Flet uygulamaları WSL2'de çalıştırılabilir. `cannot open display (ekran açılamıyor)` hatası alıyorsanız, sorun giderme için [bu kılavuza](https://github.com/microsoft/wslg/wiki/Diagnosing-%22cannot-open-display%22-type-issues-with-WSLg) göz atın.  

# Temel uygulama yapısı

Çok minimal bir Flet uygulaması aşağıdaki yapıya sahiptir:

```python
import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    pass

ft.app(target=main)
```

![](https://flet.dev/img/docs/getting-started/basic-app-structure.png)

> **NOT:**
> 
> Bu kılavuzda daha sonra yeniden kullanılabilir **kontrollerle** uygulama yapısına gerçek dünya yaklaşımları yönünden bakacağımız için bu bölüm kasıtlı olarak "**temel**" olarak adlandırılmıştır.

Tipik bir Flet programı, uygulamanın yeni kullanıcı oturumlarını beklemeye başladığı `flet.app()` çağrısıyla sona erer. `main()` fonksiyonu, bir Flet uygulamasındaki giriş noktasıdır. `Page (Sayfa)` örneğinin aktarıldığı her kullanıcı oturumu için yeni bir iş parçacığı çağrılıyor. Flet uygulamasını tarayıcıda çalıştırırken, açılan her sekme veya sayfa için yeni bir kullanıcı oturumu başlatılır. Bir masaüstü uygulaması olarak çalışırken oluşturulan yalnızca bir oturum vardır.

`Page (Sayfa)`, kullanıcıya özgü bir "**canvas (tuval)**" gibidir, kullanıcı oturumunun görsel halidir. Bir uygulama arabirimi oluşturmak için bir sayfaya (page) kontroller ekler ve kaldırırsınız, kontrollerin özelliklerini güncellersiniz. Yukarıdaki kod örneği, içerisine hiçbir kontrol eklenmediği için her kullanıcıya sadece boş bir sayfa (page) görüntüleyecektir.

Flet uygulaması, varsayılan olarak, yerel işletim sistemine penceresinde başlar. Ancak, `flet.app` çağrısını aşağıdaki gibi değiştirerek onu yeni bir tarayıcı penceresinde açabilirsiniz:

```python
ft.app(target=main, view=ft.WEB_BROWSER)
```

> **NOT**:
> 
> Dahili olarak, her Flet uygulaması bir web uygulamasıdır ve yerel bir işletim 
> sistemi penceresinde açılsa bile yerleşik bir web sunucusu arka planda başlatılır. Flet web sunucusuna "**Fletd**" adı verilir ve varsayılan olarak rastgele bir **TCP** bağlantı noktasını dinler. Özel bir TCP bağlantı noktası belirtebilir ve ardından uygulamayı masaüstü görünümüyle birlikte tarayıcıda açabilirsiniz:
> 
> ```python
> flet.app(port=8550, target=main)
> ```
> 
> Flet uygulamanızın web sürümünü görmek için tarayıcınızda `http://localhost:<port>` öğesini açın.



# Kontroller
