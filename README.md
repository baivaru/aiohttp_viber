# aioHTTP Viber
aioHTTP Viber bot is a fully async viber bot written on basis of [Viber REST API](https://developers.viber.com/docs/api/rest-bot-api/).

## Cloning & Run:
1. `git clone https://github.com/eyaadh/aiohttp_viber.git`, to clone and the repository.
2. `cd aiohttp_viber`, to enter the directory.
3. `pip3 install -r requirements.txt`, to install dependencies/requirements.
4. create a new `config.ini` file using the sample available at `viber/working_dir`
5. Run with `python3.8 -m viber`, stop with <kbd>CTRL</kbd>+<kbd>C</kbd>.
> It is recommended to use [virtual environments](https://docs.python-guide.org/dev/virtualenvs/) while running the app, this is a good practice you can use at any of your python projects as virtualenv creates an isolated Python environment which is specific to your project.

The REST API is designed to use webhooks for receiving callbacks and user messages from Viber. For security reasons only URLs with valid and official SSL certificate from a trusted CA is allowed.
In case you wish to test local you could make use of [ngrok](https://ngrok.com/) and create a public tunnel.
> Note that free version of Ngrok expires the public tunnel every 8hrs.


## Viber API & Messaging Flow:
![.](https://developers.viber.com/docs/img/send_and_receive_message_flow.png)
> More details on available Endpoints and API can be found [here](https://developers.viber.com/docs/api/rest-bot-api/).

