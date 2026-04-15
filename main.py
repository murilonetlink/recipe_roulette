import flet as ft
from ui.views.login_view import LoginView
from ui.views.roleta_view import RoletaView
from ui.views.add_view import AddRecipeView

def main(page: ft.Page):
    # Configurações do layout mobile
    page.title = "Recipe Roulette"
    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False
    
    # Tema focado nos tons de verde solicitados
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.GREEN_500,
        font_family="Roboto" # Material Design standard
    )

    def route_change(route):
        page.views.clear()
        
        # Rotas
        if page.route == "/":
            page.views.append(LoginView(page))
        elif page.route == "/roleta":
            # Protege a rota
            if not page.session.get('user_id'):
                page.go("/")
                return
            page.views.append(RoletaView(page))
        elif page.route == "/add":
            if not page.session.get('user_id'):
                page.go("/")
                return
            page.views.append(AddRecipeView(page))
            
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Iniciliza na tela de login
    page.go("/")

if __name__ == "__main__":
    ft.app(target=main)
