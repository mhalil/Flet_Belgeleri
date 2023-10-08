# Önemli Notlar

* Tipik bir Flet programı, `flet.app()` çağrısıyla sona erer.

* `main()` fonksiyonu, bir Flet uygulamasındaki giriş noktasıdır. `Page` örneğinin aktarıldığı her kullanıcı oturumu için, yeni bir iş parçacığı çağrılır.

* Flet uygulamasını tarayıcıda çalıştırırken, açılan her sekme veya sayfa için yeni bir kullanıcı oturumu başlatılır. Bir **masaüstü uygulaması** olarak çalışırken oluşturulan **yalnızca bir oturum vardır**.

* `Page`, kullanıcıya özgü bir "**canvas (tuval)**" gibidir, kullanıcı oturumunun görsel halidir. Bir uygulama arabirimi oluşturmak için bir sayfaya (page) kontroller ekler ve kaldırırsınız, kontrollerin özelliklerini güncellersiniz.

* Flet uygulaması varsayılan olarak, yerel işletim sistemi penceresinde başlar. Ancak, `flet.app` çağrısını aşağıdaki gibi değiştirerek onu yeni bir **tarayıcı penceresinde** açabilirsiniz:

```python
ft.app(target=main, view=ft.WEB_BROWSER)
```

* Bir sayfada kontrolü görüntülemek istiyorsanız, o kontrolü sayfanın `kontroller (controls)` **listesine** eklemeli ve sayfa değişikliklerini bir tarayıcıya veya masaüstü istemcisine göndermek / güncellemek için `page.update()` öğesini çağırmalısınız:

```python
def main(page: ft.Page):        
    t = ft.Text(value="Hello, world!", color="green")    
    page.controls.append(t)    
    page.update()
```

* Satıra (Row) birden fazla **kontrol (control)** eklemek gerektiğinde (yanyana sütunvari kontrol), bu değerleri `row()` kapsayıcısı içerisine **liste** olarak yazmalıyız.

```python
  def main(page: ft.Page):
      page.add(
          ft.Row(controls=[
              ft.Text("Ankara"),
              ft.Text("Bursa"),
              ft.Text("İstanbul")
          ])
      )
```

* Her kontrolün (denetimin), Sayfa (Page) oluşturulurken, varsayılan değeri `true (doğru)` olan `visible (görünür)` özelliği ve `false (yanlış)` değerini barındıran `disabled (devre dışı)` özelliği vardır. `visible (görünür)` değerini `false (yanlış / hayır)` olarak ayarlamak, kontrolün (ve varsa tüm alt öğelerinin) bir sayfa tuvalinde oluşturulmasını tamamen engeller. Gizli kontrollere klavye veya fare ile odaklanılamaz veya seçilemez ve herhangi bir olay (event) 
  belirtemez.
