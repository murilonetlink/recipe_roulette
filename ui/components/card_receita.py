import flet as ft

def CardReceita(url: str, on_close):
    # Pode ser expandido depois para puxar título real da URL, etc.
    return ft.Card(
        elevation=10,
        content=ft.Container(
            padding=20,
            bgcolor=ft.colors.GREEN_50,
            content=ft.Column(
                controls=[
                    ft.Icon(name=ft.icons.RESTAURANT_MENU, color=ft.colors.GREEN_700, size=40),
                    ft.Text("A receita sorteada foi:", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_900),
                    ft.Text(f"Link: {url}", color=ft.colors.BLUE_700, size=16, italic=True),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Abrir Link",
                                icon=ft.icons.OPEN_IN_NEW,
                                url=url,
                                bgcolor=ft.colors.GREEN_400,
                                color=ft.colors.WHITE
                            ),
                            ft.TextButton("Voltar", on_click=on_close, icon=ft.icons.ARROW_BACK, icon_color=ft.colors.GREEN_900)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )
