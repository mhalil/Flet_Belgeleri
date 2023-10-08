import flet as ft

def main(page: ft.Page):
    baslik1 = ft.Text(value="Başlık_1")
    baslik2 = ft.Text(value="Başlık_2")
    Ad = ft.TextField()
    Soyad = ft.TextField()
    
    baslik2.visible = False
    Ad.disabled = False
    Soyad.disabled = True

    page.add(baslik1, baslik2, Ad, Soyad)

ft.app(target=main)