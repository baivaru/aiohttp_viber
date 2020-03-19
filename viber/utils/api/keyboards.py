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

    @staticmethod
    async def foursquare_keyboard(venues):
        buttons = []
        for venue in venues:
            buttons.append(
                {
                    "Columns": 2,
                    "Rows": 2,
                    "ActionType": "",
                    "ActionBody": f"{venue['lat']},{venue['lon']},{venue['contact']},{venue['name']}",
                    "BgColor": "#ffffff",
                    "Image": "https://cdn.jim-nielsen.com/watchos/512/foursquare-2015-06-15.png"
                }
            )
            buttons.append(
                {
                    "Columns": 4,
                    "Rows": 2,
                    "ActionType": "reply",
                    "ActionBody": f"{venue['lat']},{venue['lon']},{venue['contact']},{venue['name']}",
                    "BgColor": "#ffffff",
                    "Text": f"<b>{venue['name']}</b><br>"
                            f"{venue['address'] if venue['address'] else ''}<br>"
                            f"{venue['street'] if venue['street'] else ''}",
                    "TextHAlign": "left",
                    "TextVAlign": "top"
                }
            )

        keyboard_obj = {
            "Type": "keyboard",
            "Buttons": buttons
        }

        return keyboard_obj

    @staticmethod
    async def admin_keyboard(users):
        buttons = []
        for user in users:
            buttons.append(
                {
                    "Columns": 3,
                    "Rows": 2,
                    "Text": f"<font color=\"#494E67\">{user['name']}</font><br><br>",
                    "TextSize": "medium",
                    "TextHAlign": "center",
                    "TextVAlign": "bottom",
                    "ActionType": "reply",
                    "ActionBody": f"{user['user_id']}",
                    "BgColor": "#f7bb3f",
                    "Image": "https://vignette.wikia.nocookie.net/the-ashtron-gaming/images/6/6d/No_image.png"
                }
            )

        keyboard_obj = {
            "Type": "keyboard",
            "Buttons": buttons
        }

        return keyboard_obj
