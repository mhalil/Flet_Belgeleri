# Büyük listeler

Çoğu  durumda listeleri görüntülemek için [Sütun (Column)](https://flet.dev/docs/controls/column) ve [Satır (Row)](https://flet.dev/docs/controls/row) kontrollerini 
kullanabilirsiniz, ancak liste, yüzlerce veya binlerce öğe içeriyorsa **Sütun** ve **Satır**, verileri, uygulamanın mevcut ekranında (kaydırma konumunda) görünmese bile tüm öğeleri bir kerede oluşturdukları için, kullanıcı arabirimi, gecikmeli olarak tepkisiz kalacak yani etkisiz olacaktır. 

Aşağıdaki örnekte, bir sayfaya 5.000 metin denetimi ekliyoruz. Sayfa, varsayılan düzen kapsayıcısı (container) olarak `Column (Sütun)`'u kullanır:

```python
import flet as ft

def main(page: ft.Page):
    for i in range(5000):
        page.controls.append(ft.Text(f"Line {i}"))
    page.scroll = "always"
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
```

Programı (kodu) çalıştırın ve bir sayfadaki tüm metin satırlarını başlangıçta yükleyip 
işlemenin yalnızca birkaç saniye sürmediğini, kaydırmanın da yavaş ve gecikmeli olduğunu fark edin:

![](https://flet.dev/img/docs/getting-started/scroll-column.gif)

Çok  sayıda öğeye sahip listeleri görüntülemek için, yalnızca mevcut 
kaydırma konumunda görünür olan öğeleri isteğe bağlı olarak işleyen 
[ListView (ListeGörünümü)](https://flet.dev/docs/controls/listview) ve [GridView (IzgaraGörünümü)](https://flet.dev/docs/controls/gridview) kontrollerini kullanın.

# ListView (ListeGörünümü)

[ListView (ListeGörünümü)](https://flet.dev/docs/controls/listview) dikey (varsayılan) veya yatay olabilir. ListView öğeleri, kaydırma yönünde birbiri ardına görüntülenir.

ListView, zaten alt öğelerinin isteğe bağlı olarak işlenmesinde etkilidir, ancak tüm öğeler ("kapsam") için aynı sabit yükseklik veya genişliği (`horizontal (yatay)` ListView için) ayarlayabilirseniz kaydırma performansı daha da iyileştirilebilir. Bu, `item_extent` özelliğiyle mutlak kapsamı ayarlayarak veya `first_item_prototype` öğesini `True` olarak ayarlayarak tüm alt öğelerin kapsamını ilk alt öğe kapsamına eşit hale getirerek yapılabilir.

ListView (ListeGörünümü) kontrolünü kullanarak 5.000 öğelik bir liste çıkaralım:

```python
import flet as ft

def main(page: ft.Page):
    lv = ft.ListView(expand=True, spacing=10)
    for i in range(5000):
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)

ft.app(target=main, view=ft.WEB_BROWSER)
```

Artık kaydırma düzgün ve fare hareketlerini takip edecek kadar hızlı:

![](https://flet.dev/img/docs/getting-started/scroll-listview.gif)

> **NOT**:
> 
> ListView yapıcısında `expand=True` kullandık. Düzgün çalışması için ListView'ün belirtilen bir yüksekliği (ya da `horizontal (yataysa)` genişliği) olması gerekir. 
> Mutlak bir boyut ayarlayabilirsiniz, örn. `ListView(height=300, space=10)`, ancak yukarıdaki örnekte ListView'ün sayfadaki tüm kullanılabilir alanı almasını sağlıyoruz, yani genişletiyoruz. [`Control.expand`](https://flet.dev/docs/controls#expand) özelliği hakkında daha fazlasını okuyun.

# GridView (IzgaraGörünümü)

GridView (IzgaraGörünümü), kontrollerin kaydırılabilir bir ızgarada düzenlenmesine izin verir.

`ft.Column(wrap=True) `veya `ft.Row(wrap=True)` ile bir "**grid (ızgara)**" oluşturabilirsiniz, örneğin:

```python
import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    r = ft.Row(wrap=True, scroll="always", expand=True)
    page.add(r)

    for i in range(5000):
        r.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
```

![](https://flet.dev/img/docs/getting-started/row-wrap-as-grid.png)

Tarayıcı penceresini kaydırmayı ve yeniden boyutlandırmayı deneyin - her şey çalışıyor, ancak çok gecikmeli.

> **NOT**:
> 
> Programın  başlangıcında, `FLET_WS_MAX_MESSAGE_SIZE` ortam değişkeninin değerini `8000000` olarak ayarlıyoruz - bu, Flet Sunucusu tarafından sayfayı 
> işleyerek alınabilecek bayt cinsinden WebSocket mesajının maksimum boyutudur. Varsayılan boyut 1 MB'dir, ancak 5.000 kapsayıcı denetimini 
> açıklayan JSON mesajının boyutu 1 MB'ı aşacaktır, bu nedenle izin verilen boyutu 8 MB'a çıkarıyoruz.
> 
> Büyük mesajları WebSocket kanalı aracılığıyla sıkıştırmak genellikle iyi bir fikir değildir, bu nedenle kanal yükünü kontrol etmek için aşağıda alnlatılan **Toplu Güncellemeleri (Batch updates)** kullanın.

GridView ListView'e benzer, birçok alt öğeyi işlemek için çok etkilidir. Yukarıdaki örneği GridView kullanarak uygulayalım:

```python
import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
```

![](https://flet.dev/img/docs/getting-started/grid-view.png)

GridView ile kaydırma ve pencere yeniden boyutlandırma sorunsuz ve duyarlı!

`run_count` özelliği ile sabit sayıda satır veya sütun (çalışma) veya `max_extent` 
özelliği ile bir "döşemenin" maksimum boyutunu belirleyebilirsiniz, böylece çalıştırma sayısı otomatik olarak değişebilir. Örneğimizde, maksimum karo boyutunu 150 piksele ayarladık ve şeklini `child_aspect_ratio=1` ile "kare" olarak ayarladık. `child_aspect_ratio`, çapraz eksenin, her alt öğenin ana eksen kapsamına oranıdır. Bu değeri `0,5` veya `2` olarak değiştirmeyi deneyin. (değeri `0.5` olarak ayarladığımızda dikey doğrultusa, `2` alarak ayarladığımızda ise yatay doğrultusa dikdörtgen elde ederiz.)

# Toplu Güncellemeler (Batch updates)

`page.update()` çağrıldığında, son `page.update()`'den bu yana sayfa güncellemelerini 
içeren WebSockets üzerinden Flet sunucusuna bir mesaj gönderilmektedir. Binlerce
 ek kontrol içeren büyük bir mesaj göndermek, kullanıcının mesajlar tamamen alınana ve kontroller sağlanana kadar birkaç saniye beklemesine neden olabilir.

Programınızın kullanılabilirliğini artırmak ve sonuçları bir kullanıcıya en kısa sürede sunmak için sayfa güncellemelerini toplu olarak gönderebilirsiniz. Örneğin, aşağıdaki program, 500 öğelik gruplar halinde bir ListView'e 5.100 alt denetim ekler:

```python
import flet as ft

def main(page: ft.Page):

    # add ListView to a page first
    lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lv)

    for i in range(5100):
        lv.controls.append(ft.Text(f"Line {i}"))
        # send page to a page
        if i % 500 == 0:
            page.update()
    # send the rest to a page
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)
```

![](https://flet.dev/img/docs/getting-started/sending-page-updates-in-batches.png)
