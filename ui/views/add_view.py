import flet as ft
from services.recipe_service import add_recipe

def AddRecipeView(page: ft.Page):
    
    def on_add(e):
        user_id = page.session.get('user_id')
        if not user_id:
            page.go("/")
            return

        if not url.value:
            page.snack_bar = ft.SnackBar(ft.Text("Cole um link primeiro!", color=ft.colors.WHITE), bgcolor=ft.colors.RED_500)
            page.snack_bar.open = True
            page.update()
            return
            
        try:
            add_recipe(user_id, url.value, category.value)
            page.snack_bar = ft.SnackBar(ft.Text("Receita salva com sucesso!", color=ft.colors.WHITE), bgcolor=ft.colors.GREEN_600)
            page.snack_bar.open = True
            
            # Limpar form
            url.value = ""
            category.value = "doce"
            
            page.go("/roleta")
        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao salvar: {str(ex)}", color=ft.colors.WHITE), bgcolor=ft.colors.RED_500)
            page.snack_bar.open = True
        
        page.update()

    def go_back(e):
        page.go("/roleta")

    url = ft.TextField(label="Link do TikTok / Instagram / YouTube", icon=ft.icons.LINK, color=ft.colors.GREEN_900)
    
    category = ft.RadioGroup(
        value="salgado",
        content=ft.Row(
            controls=[
                ft.Radio(value="doce", label="Doce"),
                ft.Radio(value="salgado", label="Salgado")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    return ft.View(
        "/add",
        controls=[
            ft.AppBar(
                title=ft.Text("Nova Receita", color=ft.colors.GREEN_900),
                bgcolor=ft.colors.GREEN_100,
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_back)
            ),
            ft.Container(
                alignment=ft.alignment.center,
                padding=30,
                content=ft.Column(
                    controls=[
                        ft.Icon(ft.icons.ADD_PHOTO_ALTERNATE, size=60, color=ft.colors.GREEN_400),
                        ft.Text("Guarde aquela receita deliciosa para depois!", size=18, color=ft.colors.GREEN_800, text_align=ft.TextAlign.CENTER),
                        ft.Divider(color=ft.colors.TRANSPARENT),
                        url,
                        ft.Text("Categoria da receita:", color=ft.colors.GREEN_900),
                        category,
                        ft.ElevatedButton("Salvar Receita", icon=ft.icons.SAVE, on_click=on_add, bgcolor=ft.colors.GREEN_500, color=ft.colors.WHITE)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        bgcolor=ft.colors.GREEN_50
    )
