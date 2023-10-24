# import modules
from flet import *
import openai
import time
from typing import Any

# make sure you generate an API key from OpenAI site
openai.api_key = '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'


def main_style() -> dict[str, Any]:
    return {
        'width': 420,
        'height': 500,
        'bgcolor': '#141518',
        'border_radius': 10,
        'padding': 15,
    }


def prompt_style() -> dict[str, Any]:
    return {
        'width': 420,
        'height': 40,
        'border_color': 'white',
        'content_padding': 10,
        'cursor_color': 'white'
    }


# main content area class
class MainContentArea(Container):

    def __init__(self) -> None:
        super().__init__(**main_style())
        self.chat = ListView(
            expand=True,
            height=200,
            spacing=15,
            auto_scroll=True
        )
        self.content = self.chat


class CreateMessage(Column):
    def __init__(self, name: str, message: str) -> None:
        self.name = name
        self.message = message
        self.text = Text(self.message)
        super().__init__(spacing=4)
        self.controls = [
            Text(self.name, opacity=0.6),
            self.text
        ]


# user input class
class Prompt(TextField):

    def __init__(self, chat: ListView) -> None:
        super().__init__(**prompt_style(), on_submit=self.run_prompt)
        self.chat = chat

    def animate_text_output(self, name: str, prompt: str) -> None:
        word_list: list = []
        msg = CreateMessage(name, '')
        self.chat.controls.append(msg)

        for word in list(prompt):
            word_list.append(word)
            msg.text.value = ''.join(word_list)
            self.chat.update()
            time.sleep(0.008)

    def user_output(self, prompt):
        self.animate_text_output(name='Me', prompt=prompt)

    def gpt_output(self, prompt):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )

        response = response.choices[0].message.content.strip()
        self.animate_text_output(name='ChatGPT', prompt=response)

    def run_prompt(self, event) -> None:
        text = event.control.value
        self.user_output(prompt=text)
        self.gpt_output(prompt=text)
        self.value = ''
        self.update()


def main(page: Page) -> None:
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.DARK

    main = MainContentArea()
    prompt = Prompt(chat=main.chat)

    page.add(
        Text('Python ChatGPT - Flet App', size=28, weight=FontWeight.W_800),
        main,
        Divider(height=6, color=colors.TRANSPARENT),
        prompt
    )
    page.update()


if __name__ == '__main__':
    app(target=main)
