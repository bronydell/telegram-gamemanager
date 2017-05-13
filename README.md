## ABOUT telegram-gamemanager

This script allows you to call your games from inline chat in Telegram and manage them.
You can have unlimited count of games and you don't have to worry about delivering it to user

### Feel free to contribute in this little project

## INSTALLATION

1. Install Python 3 on your server
    `sudo apt-get update`
    `sudo apt-get install python3`
2. Install setup tools
    `sudo apt-get install python3-setuptools`
    `sudo easy_install3 pip`
3. Clone repository using `git clone` or download zip file
4. Install dependence manually or use setup.py
    `sudo pip3 install python-telegram-bot`
5. Edit bot.json
    In `key` field put your key. You had to created it with @botfather
    In `admins` array put telegram id, owner of this id'll be an admin
    In `games` array add or remove games
    The template for the games looks like this:
    
    ```json
    {
      "name": "<GAME NAME>",
      "play_text": "<GAME SHORT DESCRIPTION>",
      "game_short_name": "<GAME'S SHORT NAME THAT YOU'VE CREATED WITH @botfather>",
      "url": "<GAME URL>"
    }
    ```
    
    For example:
    
    ```json
      "games":[
        {
          "name": "GAME A",
          "play_text": "Play GAME A",
          "game_short_name": "game_a",
          "url": "<url_to_a_game>"
        },
        {
          "name": "GAME B",
          "play_text": "Play GAME B",
          "game_short_name": "game_b",
          "url": "<url_to_a_game>"
        }
      ]
    ```
    
    You can find this example in repo.

6. Launch the script using `python3 run.py`
7. That's it!

## LICENSE
> Copyright (c) 2017 NIKISHIN ROSTISLAV

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
