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



## Linux
