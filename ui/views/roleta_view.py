import flet as ft
from ui.components.roleta import RoletaComponent

def RoletaView(page: ft.Page):
    
    category_dropdown = ft.Dropdown(
        label="O que vocês querem comer?",
        options=[
            ft.dropdown.Option("qualquer", text="Qualquer Coisa"),
            ft.dropdown.Option("doce", text="Doce"),
            ft.dropdown.Option("salgado", text="Salgado")
        ],
        value="qualquer",
        width=300,
        color=ft.colors.GREEN_900
    )

    def go_add(e):
        page.go("/add")

    def go_logout(e):
        page.session.clear()
        page.go("/")

    roleta_container = ft.Container(content=RoletaComponent(page, category_dropdown.value))
    
    # Atualiza o componente filho da roleta quando trocar o filtro
    def on_category_change(e):
        roleta_container.content = RoletaComponent(page, category_dropdown.value)
        page.update()

    category_dropdown.on_change = on_category_change

    return ft.View(
        "/roleta",
        controls=[
            ft.AppBar(
                title=ft.Text("Recipe Roulette", color=ft.colors.GREEN_900),
                bgcolor=ft.colors.GREEN_100,
                actions=[
                    ft.IconButton(ft.icons.EXIT_TO_APP, on_click=go_logout, tooltip="Sair")
                ]
            ),
            ft.Container(
                alignment=ft.alignment.center,
                padding=20,
                content=ft.Column(
                    controls=[
                        category_dropdown,
                        ft.Divider(color=ft.colors.TRANSPARENT, height=40),
                        roleta_container,
                        ft.Divider(color=ft.colors.TRANSPARENT, height=40),
                        ft.ElevatedButton("Adicionar Nova Receita", icon=ft.icons.ADD, on_click=go_add, bgcolor=ft.colors.GREEN_200, color=ft.colors.GREEN_900)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        bgcolor=ft.colors.GREEN_50
    )
