# Sürükle ve Bırak

Flet'te sürükle ve bırak mekanizması oldukça basittir - bir kullanıcı [Sürüklenebilir (`Draggable`)](https://flet.dev/docs/controls/draggable) kontrolü sürüklemeye başlar ve onu [SürüklemeHedefi (`DragTarget`)](https://flet.dev/docs/controls/dragtarget)'ne "bırakır". Hem sürüklenebilir öğe hem de sürüklenebilir hedef aynı `gruba (group)` sahipse, bir sürükleme hedefi `on_accept` olay işleyicisini çağırır ve sürüklenebilir kontrol kimliğini (ID) olay verisi olarak iletir. Bu durumda sürüklenebilir öğe, sürükle ve bırak işlemi için bir kaynak "veri" görevi görür.

Aşağıdaki örneğe bir göz atalım. Aşağıdaki programda "**1**" olarak gösterilen **sol** kontrolü , "**0**" olarak gösterilen **sağ** kontrolün üzerine sürükleyebilirsiniz ve sürükleme işlemi tamamlandığında **sol** kontrol "**0**" ile değiştirilir ve **sağ** kontrol "**1**" olur:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Drag and Drop example"

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.src_id)
        # update text inside draggable control
        src.content.content.value = "0"
        # update text inside drag target control
        e.control.content.content.value = "1"
        page.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )

ft.app(target=main)
```

![drag-and-drop-number](https://flet.dev/img/docs/getting-started/drag-and-drop-number.gif)

Bu nedenle, `on_accept` olayı gerçekleştiğinde "**kaynak**" (sürüklenebilir) ve "**hedef**" (sürükleme hedefi) kontrollerine ne olacağını belirlemek geliştiricinin  sorumluluğundadır.

> **Şunu Deneyin**:
> 
> Sürükleme hedefinin (DragTarget) grup özelliğini `number 1 (sayı 1)` olarak değiştirin ve hedefe "1" nesnesini sürükleyip bıraktığınızda, artık `on_accept`'in çağrılmadığına dikkat edin.

Sürükle ve bırak işlemini daha etkileşimli hale getirmek için ek özellikler ve olay işleyicileri vardır. Örneğin sürüklenebilir kontrol (draggable) , sürükleme işlemi devam ederken `content (içerik)` yerine farklı bir denetim görüntülemek için `content_When_dragging` özelliğine sahiptir. İşaretçi  altında farklı bir denetim göstermek için `content_feedback` özelliği de vardır. Varsayılan olarak, aynı `content (içerik)` kontrolü, ancak %50 opaklıkla sürüklenirken imlecin altında görüntülenir.

Sürüklenen kontrolün yerine bir "**boşluk**" ve sürükleme esnasında imlecin altında sadece "**1**" ifadesi gösterecek şekilde örneğimizde Draggable'ı değiştirelim:

```python
...
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=ft.Text("1"),
                ),
...
```

![drag-and-drop-number-2](https://flet.dev/img/docs/getting-started/drag-and-drop-number-2.gif)

Sürükleme hedefi denetimi ayrıca, hedefe bir şey "bırakmak" için iyi bir zaman 
geldiğinde daha iyi görselleştirmeye yardımcı olan `on_will_accept` ve `on_leave` olay işleyicilerine sahiptir. Gelen sürüklemeyi kabul etmeye hazır olduğunda, hedef kontrolün etrafına bir sınır çizmek için örneğimizde DragTarget'ı değiştirelim:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Drag and Drop example 2"

    def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.src_id)
        # update text inside draggable control
        src.content.content.value = "0"
        # reset source group, so it cannot be dropped to a target anymore
        src.group = ""
        # update text inside drag target control
        e.control.content.content.value = "1"
        # reset border
        e.control.content.border = None
        page.update()

    def drag_will_accept(e):
        # black border when it's allowed to drop and red when it's not
        e.control.content.border = ft.border.all(
            2, ft.colors.BLACK45 if e.data == "true" else ft.colors.RED
        )
        e.control.update()

    def drag_leave(e):
        e.control.content.border = None
        e.control.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=ft.Text("1"),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave,
                ),
            ]
        )
    )

ft.app(target=main)
```

![drag-and-drop-number-3](https://flet.dev/img/docs/getting-started/drag-and-drop-number-3.gif)


| Önceki Bölüm                                  | Sonraki Bölüm                                                    |
| --------------------------------------------- | ---------------------------------------------------------------- |
| [<<< 06 Büyük Listeler](06_buyuk_listeler.md) | [08 Navigasyon ve Yönlendirme >>>](08_navigasyon_yonlendirme.md) |
