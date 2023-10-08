import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text("Ankara"),
            ft.Text("Bursa"),
            ft.Text("İstanbul")
        ])
    )

ft.app(target=main)