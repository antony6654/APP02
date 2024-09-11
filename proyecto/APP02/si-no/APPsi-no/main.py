import flet as ft


def main(page: ft.Page):
    page.title="¿Me perdonas?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="red"
    
    lbll=ft.Text("¿Me perdonas?",
                style=ft.TextStyle(size=40,weight="boold"))
    
    Ingl=ft.Image(src="triste.png",width=200,height=200)
    
    btn5i=ft.ElevatedButton("Si",
                            color="grenn",
                            width=100,
                            height=50)
    
    btnNo=ft.ElevatedButton("No",
                            color="red",
                            width=100,
                            height=50)
    
    page.add(
        ft.Column(
            [
                lbll,
                Ingl,
                ft.Row([btn5i,btnNo],
                    alignment=ft.MainAxisAlignment.CENTER,
                    ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20 
        )
    )


ft.app(main)
