
import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text()
    page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(5):
        t.value = f"{i+1}. Adım"
        page.update()
        time.sleep(1)

ft.app(target=main)