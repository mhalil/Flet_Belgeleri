import flet as ft

def main(page: ft.Page):
    page.title = "Row (Satır) Kontrolü"
    
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Adınız"),
            ft.ElevatedButton(text="Adımı Söyle!")
        ])
    )

ft.app(target=main)


