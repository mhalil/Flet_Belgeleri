import flet as ft

def main(sayfa: ft.Page):
    # Sayfa Başlığı
    sayfa.title = "Sayaç Uygulaması"

    # Sayfa Ebatları
    sayfa.window_height = 200
    sayfa.window_width = 300

    # Sayfanın Dikey Hizalaması
    sayfa.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Metin Alanı
    sayac_degeri = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    # sayac değerinin azaltılması fonksiyonu. 
    def eksilt(e):
        sayac_degeri.value = str(int(sayac_degeri.value) - 1)
        sayfa.update()

    # sayac değerinin artırılması fonksiyonu
    def artir(e):
        sayac_degeri.value = str(int(sayac_degeri.value) + 1)
        sayfa.update()
    
    sayfa.add(

        ft.Row(
        [
        ft.IconButton(ft.icons.REMOVE, on_click=eksilt),
        sayac_degeri,
        ft.IconButton(ft.icons.ADD, on_click=artir)
        ],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
# ft.app(target=main, view=ft.WEB_BROWSER) # Kodu tekrar çalıştırın ve şimdi anında bir web uygulamasına sahip olursunuz:
