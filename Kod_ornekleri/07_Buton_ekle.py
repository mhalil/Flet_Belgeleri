import flet as ft

def main(page: ft.Page):
    def dugmeye_tiklandi(e):
        page.add(ft.Text("TIKLANDI!"))

    page.add(ft.ElevatedButton(text="Tiklasana", on_click=dugmeye_tiklandi))    # on_click parametresine yazılan fonksiyon/metot adı, tırnak içine yazılmadı.

ft.app(target=main)