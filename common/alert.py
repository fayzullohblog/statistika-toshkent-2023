"""Telegram message sender to chat_id

import Alerter

tg_alert = Alerter(bot_token='YOUR_BOT_TOKEN', chat_id='YOUR_CHAT_ID')
or
tg_alert = Alerter.from_environment() #Recommend

method_1: tg_alert.send_message(chat_id=111222333, text='Message text')

method_2: via decorator
@tg_alert
def some_func_that_can_raise_an_exception():
    raise RuntimeError('this is an exception')


We use in except scope as:
except Exception as e:
    return tg_alert.custom_alert(text='Message text')

"""

from __future__ import annotations
from urllib import parse, request

# load_dotenv() .env file in root folder


class Alerter:
    """
    Alerter class for sending telegram messages and decorating functions for alerts.
    """

    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    @property
    def base_url(self):
        return f"https://api.telegram.org/bot{self.bot_token}"

    @classmethod
    def from_environment(cls) -> Alerter:
        try:
            token: str = "6240825083:AAGUobsTY4ZcwWtmjO7f2kR_5h3afjCQTR4"
        except KeyError as e:
            raise KeyError("ALERT_BOT_TOKEN must be set in environment variables") from e

        try:
            chat_id = "-1001763162190"
        except KeyError as exc:
            raise KeyError("ALERT_CHAT_ID must be set in environment variables") from exc

        return cls(bot_token=token, chat_id=int(chat_id))

    def custom_alert(
        self,
        text: str,
        *,
        parse_mode: str = "HTML",
        disable_web_page_preview: bool = True,
        disable_notification: bool = False,
    ):
        """
        Sends a telegram message to default chat_id. All params according to https://core.telegram.org/bots/api#sendmessage

        :param text: message text
        :param parse_mode: None, 'MARKDOWN' or 'HTML'
        :param disable_web_page_preview: no link preview
        :param disable_notification: send silently
        :return: requests.Response
        """
        return self.send_message(
            chat_id=self.chat_id,
            text=f"🚫<b> STATISKEA  </b> <b>Error message text</b> ❌ \n\n <i>{text}</i> \n\n🐞<b>Please KILL this bug now</b> ‼️",
            parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
        )

    def send_message(
        self,
        chat_id: int,
        *,
        text: str,
        parse_mode: str = None,
        disable_web_page_preview: bool = True,
        disable_notification: bool = False,
    ):
        """
        Sends a telegram message to `chat_id`. All params according to https://core.telegram.org/bots/api#sendmessage

        :param chat_id: telegram chat id to send to
        :param text: message text
        :param parse_mode: None, 'MARKDOWN' or 'HTML'
        :param disable_web_page_preview: no link preview
        :param disable_notification: send silently
        :return: requests.Response
        """
        url = f"{self.base_url}/sendMessage"
        params = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": disable_web_page_preview,
            "disable_notification": disable_notification,
        }
        params_data = parse.urlencode(params).encode()
        req = request.Request(url, method="POST", data=params_data)
        return request.urlopen(req)


# Create object
tg_alert = Alerter.from_environment()
# We use in:
# except Exception as e:
#     return tg_alert.custom_alert(text=e)
