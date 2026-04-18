import flet as ft
import traceback

def main(page: ft.Page):
    # Configurações do layout mobile
    page.title = "Recipe Roulette"
    
    # REMOVIDO: page.window_width e page.window_height
    # O Flet agora vai herdar 100% da tela do seu S25 Ultra dinamicamente.
    
    # Adicionado scroll adaptativo para evitar que o teclado esmague a tela
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.GREEN_500,
        font_family="Roboto" 
    )

    try:
        from ui.views.login_view import LoginView
        from ui.views.roleta_view import RoletaView
        from ui.views.add_view import AddRecipeView

        def route_change(route):
            page.views.clear()
            
            if page.route == "/":
                page.views.append(LoginView(page))
            elif page.route == "/roleta":
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
        
        page.go("/")

    except Exception as e:
        page.scroll = ft.ScrollMode.AUTO
        page.add(
            ft.Text("Ocorreu um Erro Fatal:", color=ft.colors.RED_900, weight=ft.FontWeight.BOLD),
            ft.Text(traceback.format_exc(), color=ft.colors.RED_500, size=12, selectable=True)
        )
        page.update()

if __name__ == "__main__":
    ft.app(target=main)
