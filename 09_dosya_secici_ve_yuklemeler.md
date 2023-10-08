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

Uygulamanızın düzenini etkilememesi için dosya seçiciyi `page.overlay.controls` koleksiyonuna eklemeniz önerilir. Dosya seçici 0x0 boyutuna sahip olmasına rağmen, `Row` (Satır) veya `Column` (Sütuna) yerleştirildiğinde hala bir kontrol olarak kabul edilir.

```python
import flet as ft

file_picker = ft.FilePicker()
page.overlay.append(file_picker)
page.update()
```

Dosya seçici iletişim kutusunu açmak için üç yöntemden birini arayın:

- `pick_files()`
- `save_file()`
- `get_directory_path()`

Lambda bunun için oldukça iyi çalışıyor:

```python
ft.ElevatedButton("Choose files...",
    on_click=lambda _: file_picker.pick_files(allow_multiple=True))
```

İletişim kutusu kapatıldığında, aşağıdaki özelliklerden birine sahip olan olay nesnesinin `FilePicker.on_result` olay işleyicisi çağrılır:

* `files` - Yalnız "**Dosyaları seç**" iletişim kutusu, seçilen dosyaların listesi veya iletişim kutusu iptal edilmişse `None`.
- `path` "**Dosyayı kaydet**" ve "**Dizin al**" iletişim kutuları, bir dosyanın veya 
  dizinin tam yolu veya iletişim kutusu iptal edilmişse `None`.

```python
import flet as ft

def on_dialog_result(e: ft.FilePickerResultEvent):
    print("Selected files:", e.files)
    print("Selected file or directory:", e.path)

file_picker = ft.FilePicker(on_result=on_dialog_result)
```

Son sonuç her zaman `FilePicker.result` özelliğinde mevcuttur.

Mevcut tüm iletişim yöntemleri ve bunların parametreleri için [Dosya seçici](https://flet.dev/docs/controls/filepicker) kontrol belgelerini kontrol edin.

# Dosya yükleme
