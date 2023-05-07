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

Güvenilir  bir navigasyon oluşturmak için, programda geçerli rotaya bağlı olarak 
bir görünüm listesi oluşturan tek bir yer olmalıdır. Başka bir deyişle, navigasyon geçmişi yığını (görüntüler listesiyle temsil edilir) bir rotanın bir fonksiyonu olmalıdır.

Burası `page.on_route_change` olay işleyicisidir.

Her şeyi iki sayfa arasında gezinmeye izin veren eksiksiz bir örnekte bir araya getirelim:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)
```

"Visit Store (Mağazayı Ziyaret Et)" ve "Go Home (Eve Git)" düğmelerini, Web Tarayıcının (Browser) Geri/İleri düğmelerini kullanarak, URL'deki rotayı manuel olarak değiştirerek sayfalar arasında gezinmeyi deneyin - ne olursa olsun çalışır! :)

> **NOT**:
> 
> Sayfalar arasında "gezinmek" için `page.go(route)` kullandık - `page.route`'u 
> güncelleyen yardımcı bir yöntem, görünümleri güncellemek için `page.on_route_change` olay işleyicisini çağırır ve son olarak `page.update()`'i çağırır.

`page.on_view_pop`  olay işleyicisinin kullanımına dikkat edin. Kullanıcı, `AppBar` 
kontrolünde otomatik "Geri" düğmesini tıkladığında tetiklenir. İşleyicide, son öğeyi görünümler koleksiyonundan kaldırırız ve görünümün "altında (under)" köküne gideriz.

# Rota şablonları

Flet, ExpressJS benzeri yolların eşleştirilmesine ve parametrelerinin ayrıştırılmasına izin veren, [repath (yeniden yol)](https://github.com/nickcoutsos/python-repath) kitaplığına dayalı bir yardımcı sınıf olan `TemplateRoute`'u sunar, örneğin `/account/:account_id/orders/:order_id`.

`TemplateRoute`, rota değiştirme olayıyla harika oynuyor:

```python
troute = TemplateRoute(page.route)

if troute.match("/books/:id"):
    print("Book view ID:", troute.id)
elif troute.match("/account/:account_id/orders/:order_id"):
    print("Account:", troute.account_id, "Order:", troute.order_id)
else:
    print("Unknown route")
```

[Burada](https://github.com/nickcoutsos/python-repath#parameters) `repath` kitaplığı tarafından desteklenen şablon sözdizimi hakkında daha fazla bilgi edinebilirsiniz.

# Web için URL stratejisi

Flet web uygulamaları, URL tabanlı yönlendirmeyi yapılandırmanın iki yolunu destekler:

* **Path [Yol]** (varsayılan) - yollar karma [hash] olmadan okunur ve yazılır. Örneğin, `fletapp.dev/path/to/view`.

* **Hash** - yollar, [hash parçasına](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax) okunur ve yazılır. Örneğin, `fletapp.dev/#/path/to/view`.

URL stratejisini değiştirmek için `flet.app()` yönteminin `route_url_strategy` parametresini kullanın, örneğin:

```python
ft.app(target=main, route_url_strategy="hash")
```

Flet Sunucusu için URL stratejisi, `path [yol]` (varsayılan) veya `hash [karma]` olarak ayarlanabilen `FLET_ROUTE_URL_STRATEGY` ortam değişkeni ile yapılandırılabilir.

| Önceki Bölüm                                   | Sonraki Bölüm                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------ |
| [<<< 07 Sürükle ve Bırak](07_surukle_birak.md) | [09 Dosya Seçici ve Yüklemeler >>>](09_DosyaSeciciVeYuklemeler.md) |
