from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Digits
from textual.containers import Vertical, Horizontal
import asyncio
from pathlib import Path
from css import css_style


class WinApp(App):

    #ruta =  Path("../style/main.tcss")

  
    #CSS_PATH = ruta
    
    CSS = css_style()
    estado_cronometro = False
    tiempo_segundos = 0


    def compose(self) -> ComposeResult:
        self.text_title = Digits( f"{00:02d}:{00:02d}:{00:02d}", id="title")

        yield  Vertical(
            self.text_title,
            Horizontal(
                Button("Iniciar", id="start"),
                Button("Dentener", id="stop"),
                id="btn_group"
            ),
            id="main"

        )
  


    
    async def on_button_pressed(self, event: Button.Pressed) -> None:

        if event.button.id == "start":
            self.estado_cronometro = True
            asyncio.create_task(self.iniciar_cronometro())

        if event.button.id == "stop":
            self.estado_cronometro = False

            
            


    async def iniciar_cronometro(self):
       

        while self.estado_cronometro:
            await asyncio.sleep(1)
            self.tiempo_segundos += 1
            self.text_title.update(self.format_time())
        

        
    def format_time(self)-> str:

        segundos_totales = self.tiempo_segundos

        horas, resto = divmod(segundos_totales, 3600)
        minutos, segundos = divmod(resto, 60)

        text = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

        return text

    
