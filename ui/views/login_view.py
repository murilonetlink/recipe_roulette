import flet as ft
from services.auth_service import login, register_user

def LoginView(page: ft.Page):
    
    def on_login(e):
        user = login(username.value, password.value)
        if user:
            # Login com sucesso, guarda userId no estado da sessao
            page.session.set('user_id', user['id'])
            page.go("/roleta")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha inválidos", color=ft.colors.WHITE), bgcolor=ft.colors.RED_500)
            page.snack_bar.open = True
            page.update()
            
    def on_register(e):
        if username.value and password.value:
            try:
                register_user(username.value, password.value)
                page.snack_bar = ft.SnackBar(ft.Text("Usuário criado com sucesso! Pode entrar.", color=ft.colors.WHITE), bgcolor=ft.colors.GREEN_600)
                page.snack_bar.open = True
            except Exception as ex:
                print(f"Erro no registro: {ex}")
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {str(ex)}", color=ft.colors.WHITE), bgcolor=ft.colors.RED_500)
                page.snack_bar.open = True
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha usuário e senha!", color=ft.colors.WHITE), bgcolor=ft.colors.RED_500)
            page.snack_bar.open = True
        page.update()

    username = ft.TextField(label="Usuário", icon=ft.icons.PERSON, color=ft.colors.GREEN_900)
    password = ft.TextField(label="Senha", password=True, can_reveal_password=True, icon=ft.icons.LOCK, color=ft.colors.GREEN_900)
    
    return ft.View(
        "/",
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                padding=50,
                content=ft.Column(
                    controls=[
                        ft.Icon(name=ft.icons.RESTAURANT, size=80, color=ft.colors.GREEN_600),
                        ft.Text("Recipe Roulette", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_800),
                        ft.Divider(color=ft.colors.TRANSPARENT),
                        username,
                        password,
                        ft.ElevatedButton("ENTRAR", on_click=on_login, width=200, bgcolor=ft.colors.GREEN_500, color=ft.colors.WHITE),
                        ft.TextButton("Criar minha conta rápida", on_click=on_register, width=200)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        ],
        bgcolor=ft.colors.GREEN_50
    )
