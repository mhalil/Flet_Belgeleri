import flet as ft

def main(page):

    ad = ft.Ref[ft.TextField]()
    soyad = ft.Ref[ft.TextField]()
    karsilama = ft.Ref[ft.Column]()

    def dugmeye_tikla(e):
        karsilama.current.controls.append(
            ft.Text(f"Merhaba, {ad.current.value} {soyad.current.value}!")
        )
        ad.current.value = ""
        soyad.current.value = ""
        page.update()
        ad.current.focus()

    page.add(
        ft.TextField(ref=ad, label="Adınız:", autofocus=True),
        ft.TextField(ref=soyad, label="Soyadınız:"),
        ft.ElevatedButton("Merhaba Diyelim!", on_click=dugmeye_tikla),
        ft.Column(ref=karsilama),
    )

ft.app(target=main)