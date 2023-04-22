# Sürükle ve Bırak

Flet'te sürükle ve bırak mekanizması oldukça basittir - bir kullanıcı [Sürüklenebilir](https://flet.dev/docs/controls/draggable) kontrolü sürüklemeye başlar ve onu [`DragTarget`](https://flet.dev/docs/controls/dragtarget)'a "bırakır". Hem sürüklenebilir öğe hem de sürüklenebilir hedef aynı `gruba (group)` sahipse, bir sürükleme hedefi `on_accept` olay işleyicisini çağırır ve sürüklenebilir kontrol kimliğini (ID) olay verisi olarak iletir. Bu durumda sürüklenebilir öğe, sürükle ve bırak işlemi için bir kaynak "veri" görevi görür.

Aşağıdaki örneğe bir göz atalım. Aşağıdaki programda "1" gösteren sol kontrolü 
"0" gösteren sağ kontrolün üzerine sürükleyebilirsiniz ve sürükleme işlemi tamamlandığında sol kontrol "0" ile değiştirilir ve sağ kontrol "1" olur:

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

![https://flet.dev/img/docs/getting-started/drag-and-drop-number.gif](https://flet.dev/img/docs/getting-started/drag-and-drop-number.gif)

Bu nedenle, `on_accept` olayı gerçekleştiğinde "kaynak" (sürüklenebilir) ve "hedef" (sürüklenecek hedef) kontrollerine ne olacağını belirlemek geliştiricinin  sorumluluğundadır.

> **Şunu Deneyin**:
> 
> Sürüklenecek hedefin (DragTarget) grup özelliğini `number 1 (sayı 1)` olarak değiştirin ve hedefe "1" düştüğünüzde artık `on_accept`'in çağrılmadığına dikkat edin.
