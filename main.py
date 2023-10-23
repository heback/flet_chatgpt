# import modules
from flet import *
import openai
import time

# make sure you generate an API key from OpenAI site
openai.api_key = ''


def main(page: Page) -> None:
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.vertical_alignment = CrossAxisAlignment.CENTER
    page.theme_mode = ThemeMode.DARK
    page.update()


if __name__ == '__main__':
    app(target=main)
