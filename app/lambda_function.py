import requests
import json


def lambda_handler(event, context):
    SlackNotice(event).send()


class SlackNotice:
    def __init__(self, content={}) -> None:
        self.set(**content)

    def set(self, url=None, level=None, title=None, text=None):
        self.url = url
        self.level = level
        self.title = title
        self.text = text
        return self

    def send(self):
        if not self.url:
            raise
        level = self.getLevel(self.level)
        color = self.getColor(level)
        text = self.toText(self.text)
        main_text = ''
        if level > 1:
            main_text = '<!channel>'
        data = {
            "text": main_text,
            "attachments": [
                {
                    "title": self.title,
                    "text": text,
                    "color": color,
                }
            ]
        }
        return requests.post(self.url, json.dumps(data))

    def getLevel(self, var):
        if var == None:
            return 0
        if type(var) == int:
            return var
        if type(var) != str:
            return 9
        if var == 'notice':
            return 1
        if var == 'warn':
            return 2
        if var == 'error':
            return 3
        return 9

    def getColor(self, level):
        if level == 0:
            return None
        if level == 1:
            return "good"
        if level == 2:
            return "warning"
        if level == 3:
            return "danger"
        return "danger"

    def toText(self, var):
        if type(var) == str:
            return var
        return str(var)
