import flet as ft
import traceback # Biblioteca para capturar o erro completo

def main(page: ft.Page):
    # Configurações do layout mobile
    page.title = "Recipe Roulette"
    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False
    
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.GREEN_500,
        font_family="Roboto" 
    )

    try:
        # Movemos as importações para DENTRO da função main.
        # Assim, se o erro for na hora de ler o Banco de Dados, 
        # a tela do app já vai estar pronta para mostrar o aviso!
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
        # Se der qualquer erro na inicialização, a tela cinza não aparece mais.
        # Ele vai imprimir o log do erro de vermelho na tela do seu celular!
        page.scroll = ft.ScrollMode.AUTO
        page.add(
            ft.Text("Ocorreu um Erro Fatal:", color=ft.colors.RED_900, weight=ft.FontWeight.BOLD),
            ft.Text(traceback.format_exc(), color=ft.colors.RED_500, size=12, selectable=True)
        )
        page.update()

if __name__ == "__main__":
    ft.app(target=main)
