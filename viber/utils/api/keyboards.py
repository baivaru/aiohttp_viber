class ViberKeyboards:
    @staticmethod
    async def gazette_keyboard(data):
        button = []
        x = 0
        for document in data[:10]:
            button.append(
                {
                    "Columns": 2,
                    "Rows": 2,
                    "ActionType": "",
                    "ActionBody": x,
                    "BgColor": "#f6f7f9",
                    "Image": "https://www.dhivehilyrics.com/images/album/13.jpg"
                }
            )
            button.append(
                {
                    "Columns": 4,
                    "Rows": 2,
                    "Text": f"<br><b>\u00A0\u00A0{document['title']}</b><br>\u00A0\u00A0{document['volume']}<br>"
                            f"\u00A0\u00A0{document['date']}",
                    "TextSize": "regular",
                    "TextHAlign": "right",
                    "TextVAlign": "center",
                    "ActionType": "reply",
                    "ActionBody": x,
                    "BgColor": "#f6f7f9"
                }
            )

            x = x + 1

        keyboard_obj = {
            "Type": "keyboard",
            "Buttons": button
        }

        return keyboard_obj
