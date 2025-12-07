from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Digits, OptionList, option_list, ContentSwitcher, Input, RadioSet,RadioButton
from textual.containers import Vertical, Horizontal
import asyncio

#from pathlib import Path
from css import css_style


class WinApp(App):

    # ruta =  Path("../style/main.tcss")


    # CSS_PATH = ruta

    CSS = css_style()
    estado_cronometro = False
    estado_cronometro_temp =  False
    tiempo_segundos = 0
    unidad_tiempo = "s"

    def compose(self) -> ComposeResult:
        self.text_title = Digits( f"{00:02d}:{00:02d}:{00:02d}", id="title")
        self.text_title_temp = Digits( f"{00:02d}:{00:02d}:{00:02d}", id="title")


        self.input_temp = Input(placeholder="Ingresar tiempo", id="input_temp")


        yield  Vertical(
            OptionList(
                option_list.Option("Home", id="home"),
                option_list.Option("Cronometro", id="crono"),
                option_list.Option("Temporizador", id="temp")
            ),
            id="menu"
        )


        with ContentSwitcher(initial="home", id="swithcer"):
            #Pantalla de inico
            with Vertical(id="home"):
                yield Label("Pantalla de inicio")


            with Vertical(id="crono"):
                yield self.text_title
                with Horizontal(id="btn_group"):
                    yield Button("Iniciar", id="start")
                    yield Button("Dentener", id="stop")
                    yield Button("Resetear", id="rest_cronometro")






            with Vertical(id="temp"):
                yield Label("Pantalla de temp")
                with RadioSet(id="group_id"):
                    yield RadioButton("Horas", id="h")
                    yield RadioButton("minutos", id="m")
                    yield RadioButton("Segundo", id="s" , value=True)

                yield self.input_temp
                yield self.text_title_temp
                yield Horizontal(
                    Button("Iniciar", id="start_temp"),
                    Button("Dentener", id="stop_temp"),
                    id="btn_group"
                )




    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        opcion = event.option.id
        if opcion == "home":
            self.query_one("#swithcer",ContentSwitcher).current =  opcion

        if opcion == "crono":
            self.query_one("#swithcer",ContentSwitcher).current =  opcion

        if opcion == "temp":
            self.query_one("#swithcer",ContentSwitcher).current =  opcion





    async def on_button_pressed(self, event: Button.Pressed) -> None:

        if event.button.id == "start":
            self.estado_cronometro = True
            asyncio.create_task(self.iniciar_cronometro())

        if event.button.id == "stop":
            self.estado_cronometro = False

        if event.button.id == "rest_cronometro":
            self.tiempo_segundos = 0
            self.text_title.update(self.format_time(self.tiempo_segundos))

        if event.button.id == "start_temp":
            self.estado_cronometro_temp = True
            asyncio.create_task(self.iniciar_temporizador())
        if event.button.id == "stop_temp":
            self.estado_cronometro_temp = False


    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        rb = event.pressed          # RadioButton que quedó activo
        self.unidad_tiempo = rb.id  # "h", "m" o "s"






    async def iniciar_cronometro(self):

        while self.estado_cronometro:
            await asyncio.sleep(1)
            self.tiempo_segundos += 1
            self.text_title.update(self.format_time(self.tiempo_segundos))

    async def iniciar_temporizador(self):
        segundo = int(self.input_temp.value)
        tiempo = self.cal_segundo(tiempo=segundo)
        while self.estado_cronometro_temp:
            self.text_title_temp.update(self.format_time(tiempo))
            if tiempo == 0:
                self.estado_cronometro_temp = False
                self.notify("Se acabo el tiempo")
                break
            await asyncio.sleep(1)
            tiempo -=1





    def format_time(self, tiempo: int)-> str:

        segundos_totales = tiempo

        horas, resto = divmod(segundos_totales, 3600)
        minutos, segundos = divmod(resto, 60)

        text = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

        return text


    def cal_segundo(self, tiempo: int) -> int:

        if self.unidad_tiempo == "h":
            return tiempo * 3600
        elif self.unidad_tiempo == "m":
            return tiempo * 60

        return tiempo
