# Navigasyon ve Yönlendirme

Gezinme  ve yönlendirme özelliği, uygulama URL'si, uygulamanın mevcut durumunu yansıtırken, kullanıcı arabiriminin sanal sayfalar (görünümler) halinde düzenlenmesine ve aralarında "gezinmeye" olanak tanıyan Tek Sayfa Uygulamalarının (Single Page Applications - SPA) temel bir özelliğidir.

Mobil uygulamalar için gezinme ve yönlendirme, belirli uygulama bölümlerine [derin bir bağlantı](https://docs.flutter.dev/ui/navigation/deep-linking)) işlevi görür.

Uygulama [Navigator 2.0](https://medium.com/flutter/learning-flutters-new-navigation-and-routing-system-7c9068155ade) Flutter API'sine dayandığından ve Flet'in "Sayfa (Page)" soyutlamasını "Sayfa ve Görünümler (Page and Views)" ile değiştirmek için gerekli olduğundan, Flet'e navigasyon ve yönlendirme eklemek beklenenden [daha fazla çaba](https://github.com/flet-dev/flet/pull/95/files) gerektirdi. Flutter'ın daha yeni gezinme ve yönlendirme API'si aşağıdakiler gibi önemli iyileştirmelere sahiptir:

1. Tarih yığını üzerinde programatik kontrol.

2. AppBar'da "Geri" düğmesine yapılan bir çağrıyı engellemenin kolay bir yolu.

3. Tarayıcı geçmişi ile sağlam senkronizasyon.
   
   

![](https://flet.dev/img/docs/navigation-routing/routing-app-example.gif)

Yukarıdaki örneğin [kaynak kodunu](https://github.com/flet-dev/examples/blob/main/python/apps/routing-navigation/building-views-on-route-change.py) keşfedin.



# Sayfa Yönlendirmesi (Rotası)

Sayfa yönlendirmesi, uygulama URL'sinin `#` sembolünden sonraki kısmıdır:

![](https://flet.dev/img/docs/navigation-routing/page-address-route.png)

Kullanıcı tarafından uygulama URL'sinde ayarlanmamışsa, varsayılan uygulama yolu `/` 
 şeklindedir. Tüm yönlendirmeler (rotalar) `/` ile başlar, örneğin `/store`, `/authors/1/books/2`.

Uygulama rotası, `page.route` özelliği okunarak elde edilebilir, örneğin:

```python
import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

ft.app(target=main, view=ft.WEB_BROWSER)
```

Uygulama URL'sini alın, yeni bir tarayıcı sekmesi açın, URL'yi yapıştırın, `/test` etmek için `#`'den sonraki kısmını değiştirin ve enter tuşuna basın. "Initial route: /test (İlk yönlendirme: / test)" ifadesini görmelisiniz.

URL'deki yönlendirme her değiştirildiğinde (URL'yi düzenleyerek veya Geri/İleri 
düğmeleriyle tarayıcı geçmişinde gezinerek) Flet, `page.on_route_change` olay işleyicisini çağırır:

```python
import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(route):
        page.add(ft.Text(f"New route: {route}"))

    page.on_route_change = route_change
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
```

Şimdi URL sağlamasını birkaç kez güncellemeyi deneyin ve ardından Geri/İleri düğmelerini kullanın! Yönlendirme her değiştiğinde sayfaya eklenen yeni bir mesajı görmelisiniz:

![](https://flet.dev/img/docs/navigation-routing/page-route-change-event.gif)

Yönlendirme, `page.route` özelliği güncellenerek programlı olarak değiştirilebilir:

```python
import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(route):
        page.add(ft.Text(f"New route: {route}"))

    def go_store(e):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))

ft.app(target=main, view=ft.WEB_BROWSER)
```

"Go to Store (Mağazaya Git)" düğmesini tıklayın ve uygulama URL'sinin değiştiğini ve tarayıcı geçmişinde yeni bir öğenin gönderildiğini göreceksiniz. Bir önceki yönlendirmeye gitmek için tarayıcının "Geri" düğmesini kullanabilirsiniz.



# Sayfa Görünümleri

Flet'in [Sayfası (Page)](https://flet.dev/docs/controls/page) artık yalnızca tek bir sayfa değil, aynı zamanda bir sandviç 
gibi üst üste yerleştirilmiş bir [görünüm](https://flet.dev/docs/controls/view) kapsayıcıdır:



![](https://flet.dev/img/docs/navigation-routing/page-views.svg)

Bir görünüm koleksiyonu, gezgin geçmişini temsil eder. Sayfa (Page), görünüm koleksiyonuna erişmek için `page.views` özelliğine sahiptir.

Listedeki son görünüm, o anda bir sayfada görüntülenen görünümdür. Görünümler 
listesi en az bir öğeye (kök görünüm) sahip olmalıdır.

Sayfalar arasında geçişi simüle etmek için `page.route`'u değiştirin ve `page.view` listesinin sonuna yeni bir Görünüm (View) ekleyin.

Koleksiyondan son görünümü açın ve geri gitmek için `page.on_view_pop` olay 
işleyicisinde yönlendirmeyi "önceki (previous)" bir görünümle değiştirin.



# Güzergah değişikliğinde görünüm oluşturma


