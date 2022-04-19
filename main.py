import discum  
import ctypes 
import json
import string   
import random
import os
import time
import datetime 

from pypresence import Presence
from colorama import Style, Fore, init
from datetime import date
from datetime import datetime



init()
os.system(f'mode 85,20')
randomm = ''.join((random.choice(string.ascii_lowercase) for x in range(5)))
message_logging = f"true"

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')

bot = discum.Client(token=token, log=False)

def main():
    @bot.gateway.command
    def get_user(resp):
        if resp.event.ready_supplemental:
            user = bot.gateway.session.user
            ctypes.windll.kernel32.SetConsoleTitleW("[Flame Logger] - Connected as: {}#{} - ({})".format(user['username'], user['discriminator'], user['id']))
            username = ("{}#{}".format(user['username'], user['discriminator']))
            id = ("{}".format(user['id']))
            print(f'''
                                  \033[37m╔═╗ ╦   ╔═╗ ╔╦╗ ╔═╗  
                                  \033[90m╠╣  ║   ╠═╣ ║║║ ║╣   
                                  {Fore.RED}╚   ╩═╝ ╩ ╩ ╩ ╩ ╚═╝ 

                            {Fore.RED}╔═════════════════════════════════╗
                               \033[37mUser{Fore.RED}:    \033[37m[{Fore.RED}{username}\033[37m]
                               \033[37mID{Fore.RED}:      \033[37m[{Fore.RED}{id}\033[37m]
                               \033[37mGuilds{Fore.RED}:  \033[37m[{Fore.RED}{len(bot.gateway.session.guilds)}\033[37m]
                            {Fore.RED}╚═════════════════════════════════╝
            ''')
    checks()

def checks():
    if message_logging == 'true':
        @bot.gateway.command
        def meesage_logs(resp):
            if resp.event.message:
                m = resp.parsed.auto()
                guildID = m['guild_id'] if 'guild_id' in m else None 
                channelID = m['channel_id']
                username = m['author']['username']
                discriminator = m['author']['discriminator']
                content = m['content']
                try:
                    guild = bot.gateway.session.guild(guildID)
                    guildName = guild.name
                    channel = bot.getChannel(channelID).json()
                    channelName = channel["name"]
                except:
                    pass
                
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")             
                today = date.today()
                message_logging_file = f'FlameLogger/{randomm}_{today}.txt'
                
                with open(message_logging_file, "a") as f:
                    try:
                        f.write("[Flame Logger] | [{}] [{}] | Guild Name: {} | Guild ID: {} | Channel Name: {} | Channel ID: {} | Username: {}#{} | Content: {}".format(today, current_time, guildName, guildID, channelName, channelID, username, discriminator, content) + "\n")
                    except:
                        pass
    elif message_logging == 'false':
        pass
    else:
        pass


if __name__ == "__main__":
    main()
    bot.gateway.run(auto_reconnect=True)
