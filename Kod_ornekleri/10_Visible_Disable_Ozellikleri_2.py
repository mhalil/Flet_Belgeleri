import flet as ft

def main(page: ft.Page):
    Ad = ft.TextField()
    Soyad = ft.TextField()

    sutun = ft.Column(controls=[
        Ad,
        Soyad
    ])

    sutun.disabled = True
    
    page.add(sutun)

ft.app(target=main)