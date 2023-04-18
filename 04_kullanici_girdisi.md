# Kullanıcıdan girdi almak

**Flet** ile etkileşimli web uygulamaları yapmak çocuk oyuncağı! Bu yalnızca verileri görüntülemekle sınırlı değildir, bir kullanıcıdan girdi talep edebilir ve sayfa kontrolleri tarafından oluşturulan çeşitli olaylara yanıt verebilirsiniz.

## Butonlar / Düğmeler

`Button` (Düğme), basıldığında oluşturan `click` (tıklama) olayı, en önemli girdi kontrolüdür:

```python
btn = ft.ElevatedButton("Click me!")
page.add(btn)
```

![buton](https://flet.dev/img/docs/getting-started/getting-user-input-elevated-button.png)

Bir web sayfasındaki kontroller tarafından oluşturulan tüm olaylar, sürekli olarak komut dosyanıza geri gönderilir, peki bir düğme tıklamasına nasıl yanıt verirsiniz?

## Olay (Etkinlik) İşleyicileri

"Sayaç (Counter)" uygulamasındaki etkinlikleri içeren düğmeler:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
```

![sayac](https://flet.dev/img/docs/getting-started/getting-user-input-event-handlers.png)

## Metin kutusu (Textbox)

**Flet**, form oluşturmak için bir dizi [kontrol](https://flet.dev/docs/controls) sağlar: [TextField (Metin Alanı)](https://flet.dev/docs/controls/textfield), [Checkbox (Onay Kutusu)](https://flet.dev/docs/controls/checkbox), [Dropdown (Açılır Menü)](https://flet.dev/docs/controls/dropdown), [ElevatedButton (Yükseltilmiş Düğme)](https://flet.dev/docs/controls/elevatedbutton).

Kullanıcıdan bir isim isteyelim:

```python
import flet as ft

def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

ft.app(target=main)
```

![metin_kutusu](https://flet.dev/img/docs/getting-started/getting-user-input-textbox.png)

## Onay Kutusu (Checkbox)

[Onay Kutusu (Checkbox)](https://flet.dev/docs/controls/checkbox) kontrolü, kullanım kolaylığı için size çeşitli özellikler ve olay yayıcılar sağlar.

Bir tek onay kutusu içeren, **Yapılacaklar (ToDo)** uygulaması oluşturalım:

```python
import flet as ft


def main(page):
    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)

ft.app(target=main)
```

![onay_kutusu](https://flet.dev/img/docs/getting-started/getting-user-input-checkbox.png)

## Açılır Menü (Dropdown)

İçerisinde **KIRMIZI**, **YEŞİL** ve **MAVİ** seçenekleri bulunan bir açılır menü oluşturalım:

```python
import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("KIRMIZI"),
            ft.dropdown.Option("YEŞİL"),
            ft.dropdown.Option("MAVİ"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)

ft.app(target=main)
```

![acilir_menu](https://flet.dev/img/docs/getting-started/getting-user-input-dropdown.png)
