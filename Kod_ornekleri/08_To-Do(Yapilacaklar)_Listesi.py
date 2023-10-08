import flet as ft

def main(page):
    def tikla_ekle(e):
        page.add(ft.Checkbox(label=yeni_gorev.value))
        yeni_gorev.value = ""
        yeni_gorev.focus()
        yeni_gorev.update()

    yeni_gorev = ft.TextField(hint_text="Neye ihtiyacın var?", width=300)
    page.add(ft.Row([yeni_gorev, ft.ElevatedButton("Ekle", on_click=tikla_ekle)]))

ft.app(target=main)