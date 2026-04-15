import flet as ft
import time
from services.recipe_service import get_random_recipe
from ui.components.card_receita import CardReceita

def RoletaComponent(page: ft.Page, category: str):
    container = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
    
    status_text = ft.Text("Preparado para o sorteio?!", size=18, color=ft.colors.GREEN_800)
    progress = ft.ProgressRing(visible=False, color=ft.colors.GREEN_400)
    
    def on_sortear(e):
        btn_sortear.disabled = True
        status_text.value = "A roleta está girando..."
        progress.visible = True
        page.update()
        
        # Simula o tempo de giro
        time.sleep(2)
        
        receita = get_random_recipe(category)
        
        progress.visible = False
        btn_sortear.disabled = False
        
        if receita:
            status_text.value = "Temos um vencedor!"
            # Exibe o modal com o resultado
            
            def close_dlg(e):
                dlg.open = False
                page.update()

            dlg = ft.AlertDialog(
                content=CardReceita(url=receita['url'], on_close=close_dlg),
                on_dismiss=lambda e: print("Fechado")
            )
            page.dialog = dlg
            dlg.open = True
        else:
            status_text.value = "Nenhuma receita encontrada para essa categoria!"
        
        page.update()

    btn_sortear = ft.ElevatedButton(
        "GIRAR A ROLETA!",
        icon=ft.icons.CASINO,
        on_click=on_sortear,
        bgcolor=ft.colors.GREEN_300,
        color=ft.colors.GREEN_900,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        )
    )
    
    container.controls = [
        status_text,
        progress,
        btn_sortear
    ]
    return container
