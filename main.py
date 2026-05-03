from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import time
import random

class SaiLayLogic(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.status_label = Label(text="[ 01 LOGIC VAULT ]\nEnter Access Key", font_size='18sp', markup=True)
        self.password_input = TextInput(hint_text="Password...", password=True, multiline=False, size_hint_y=None, height='50dp')
        self.login_btn = Button(text="VERIFY", background_color=(0, 0.7, 1, 1), size_hint_y=None, height='60dp')
        self.login_btn.bind(on_press=self.check_logic)
        
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.login_btn)
        return self.layout

    def check_logic(self, instance):
        # အောင် သတ်မှတ်လိုက်တဲ့ Password အတိအကျ
        if self.password_input.text == "Favorite four-eyed crush":
            self.status_label.text = "[color=00ff00]STATUS: 1\nSUCCESSFUL[/color]"
        else:
            self.start_trap()

    def start_trap(self):
        self.start_time = time.time()
        self.login_btn.disabled = True
        self.password_input.text = ""
        Clock.schedule_interval(self.hacker_trap_ui, 0.1)

    def hacker_trap_ui(self, dt):
        elapsed = time.time() - self.start_time
        if elapsed < 60:
            logic_rain = "".join(random.choice("01") for _ in range(15))
            self.status_label.text = f"[color=ff0000]ERROR 01\n{logic_rain}[/color]\nRetrying: {int(60-elapsed)}s"
        else:
            self.status_label.text = "[ 01 LOGIC VAULT ]\nLocked - Try Again"
            self.login_btn.disabled = False
            return False

if __name__ == "__main__":
    SaiLayLogic().run()
