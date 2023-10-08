import flet as ft

def main(page):

    ad = ft.TextField(label="Adınız:", autofocus=True)
    soyad = ft.TextField(label="Soyadınız:")
    karsilama = ft.Column()   # farklı kontrollerin yan yana gelmesi için bir sütun yapısı (konteyner (container)) tanımlıyoruz.

    def dugmeye_tikla(e):
        karsilama.controls.append(ft.Text(f"Merhaba, {ad.value} {soyad.value}!"))     # tanımlanan konteyner'a, kontrolleri ekliyoruz. 
        ad.value = ""
        soyad.value = ""
        page.update()
        ad.focus()

    page.add(
        ad,
        soyad,
        ft.ElevatedButton("Merhaba diyelim!", on_click=dugmeye_tikla),
        karsilama,
    )

ft.app(target=main)