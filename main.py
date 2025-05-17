import discord
from discord.ext import commands
from colorama import Fore
import asyncio
import os
import platform

current_os = platform.system()

intents = discord.Intents.default() 
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

print(Fore.LIGHTCYAN_EX + r"""

 ________  _____ ______           ________  ________  ________  _____ ______   _____ ______   _______   ________         
|\   ___ \|\   _ \  _   \        |\   ____\|\   __  \|\   __  \|\   _ \  _   \|\   _ \  _   \|\  ___ \ |\   __  \        
\ \  \_|\ \ \  \\\__\ \  \       \ \  \___|\ \  \|\  \ \  \|\  \ \  \\\__\ \  \ \  \\\__\ \  \ \   __/|\ \  \|\  \       
 \ \  \ \\ \ \  \\|__| \  \       \ \_____  \ \   ____\ \   __  \ \  \\|__| \  \ \  \\|__| \  \ \  \_|/_\ \   _  _\      
  \ \  \_\\ \ \  \    \ \  \       \|____|\  \ \  \___|\ \  \ \  \ \  \    \ \  \ \  \    \ \  \ \  \_|\ \ \  \\  \|     
   \ \_______\ \__\    \ \__\        ____\_\  \ \__\    \ \__\ \__\ \__\    \ \__\ \__\    \ \__\ \_______\ \__\\ _\     
    \|_______|\|__|     \|__|       |\_________\|__|     \|__|\|__|\|__|     \|__|\|__|     \|__|\|_______|\|__|\|__|    
                                    \|_________|                                                                         
                                                                                                                         
                                                                                                                         

      """)

def gatherinfo():
    while True:
        token = input(Fore.RED + "Enter Bot Token: ")
        try:
            guild_id = int(input(Fore.LIGHTWHITE_EX + "Enter Guild ID: "))
            return token, guild_id 
        except ValueError:
            print(Fore.RED + "\nInvalid guild ID!\n" + Fore.WHITE + "\n-------------\n")



async def start_bot():
    while True:
        TOKEN, GUILD_ID = gatherinfo()

        bot = commands.Bot(command_prefix="!", intents=intents)

        @bot.event
        async def on_ready():
            guild = discord.utils.get(bot.guilds, id=GUILD_ID)

            if guild is None:
                    print(f"Guild ID {GUILD_ID} not found.")
                    return
            else:
                print(Fore.CYAN + f"\nLogged in as {bot.user}")
                print(Fore.GREEN + f"Found guild: {guild.name} ({guild.id})")
                await bot.tree.sync()

                message = input(Fore.YELLOW + "\nWhat the message should be: ")
                times = int(input(Fore.MAGENTA + "How many times it should DM the users: "))

                async def send_messages(member):
                    for i in range(times):
                        try:
                            await member.send(message)
                            await asyncio.sleep(0.5)
                            print(Fore.BLUE + f"Successfully sent message to {member}")
                        except Exception:
                            print(Fore.BLUE + f"Could not DM {member}")

                tasks = [asyncio.create_task(send_messages(m)) for m in guild.members if not m.bot]
                await asyncio.gather(*tasks)

                end = input(Fore.WHITE + "\n-------------\n\nSuccessfully DMed all users. Would you like to exit? (y/n) ")
                if end.lower() != "n":
                    if current_os == "Windows":
                        os.system("cls")
                        print(Fore.BLUE + "Thank you for using our tool. Exiting in 5 seconds...")
                        await asyncio.sleep(5)
                        exit()
                    elif current_os == "Linux" or current_os == "Darwin":
                        os.system("clear")
                        print(Fore.BLUE + "Thank you for using our tool. Exiting in 5 seconds...")
                        await asyncio.sleep(5)
                        exit()
                else:
                    print(Fore.WHITE + "\n-------------\n\nI guess it's just us now.\nIf you get bored of me and want to exit, press Control + C.")
        try:
            await bot.start(TOKEN)
            return True
        except discord.LoginFailure:
            print("\nInvalid token. Please try again.\n\n-------------\n")
            #return
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(start_bot())
