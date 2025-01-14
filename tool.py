import os
import sys
import time
import webbrowser
from colorama import init, Fore, Style

init(autoreset=True)

ASCII_LOGO = Fore.WHITE + r"""
 ▄█  ███▄▄▄▄      ▄████████  ▄█  ████████▄   ▄█   ▄██████▄  ███    █▄     ▄████████ 
███  ███▀▀▀██▄   ███    ███ ███  ███   ▀███ ███  ███    ███ ███    ███   ███    ███ 
███▌ ███   ███   ███    █▀  ███▌ ███    ███ ███▌ ███    ███ ███    ███   ███    █▀  
███▌ ███   ███   ███        ███▌ ███    ███ ███▌ ███    ███ ███    ███   ███        
███▌ ███   ███ ▀███████████ ███▌ ███    ███ ███▌ ███    ███ ███    ███ ▀███████████ 
███  ███   ███          ███ ███  ███    ███ ███  ███    ███ ███    ███          ███ 
███  ███   ███    ▄█    ███ ███  ███   ▄███ ███  ███    ███ ███    ███    ▄█    ███ 
█▀    ▀█   █▀   ▄████████▀  █▀   ████████▀  █▀    ▀██████▀  ████████▀   ▄████████▀  
                                                                                    
""" + Style.RESET_ALL

class MultiTool:
    def __init__(self):
        self.options = {
            '1': "Fake Info",
            '2': "EDR Tools",
            '3': "OSINT Tools",
            '4': "Discord Tools",
            '5': "Temporary Tools",
            '6': "Movie/Show Tools",
            '7': "Other 765 Tools",
            '8': "Username Checker Tools",
            '9': "Exit Multi Tool"
        }
        self.links = {
            "fake_info": {
                "Fake ID": "https://www.fakenamegenerator.com/",
                "Fake CC": "https://www.fakenamegenerator.com/credit-card-validator.php",
                "Fake SSN": "https://www.fakenamegenerator.com/social-security-number.php",
                "Address Gen": "https://www.real-generator.com/address"
            },
            "edr_tools": {
                "Crowd Strike": "https://crowdstrike.com/",
                "Sentinel One": "https://sentinelone.com/",
                "Sophos": "https://www.sophos.com/",
                "Trend Micro": "https://www.trendmicro.com/",
                "Bit Defender": "https://www.bitdefender.com/",
                "VM Ware": "https://www.vmware.com/",
                "Fire EYE": "https://www.fireeye.com/",
                "Checkpoint": "https://www.checkpoint.com/",
                "ESET": "https://www.eset.com/",
                "Paloalto Networks": "https://www.paloaltonetworks.com/"
            },
            "osint_tools": {
                "Malt EGO": "https://www.maltego.com/",
                "Shodan": "https://www.shodan.io/",
                "The Harvester": "https://github.com/laramies/theHarvester",
                "OSINT Framework": "https://osintframework.com/",
                "OSINT Industries": "https://www.osint.industries/",
                "OSINT 4 All": "https://start.me/p/L1rEYQ/osint4all",
                "Intel Techniques": "https://inteltechniques.com/"
            },
            "discord_tools": {
                "Discord ID": "https://toolscord.com/",
                "Discord Leaks": "https://discordleaks.unicornriot.ninja/discord/",
                "Inf0Sec": "https://inf0sec.top/"
            },
            "temp_tools": {
                "Temp Mail": "https://www.temp-mail.org/",
                "Guerilla Mail": "https://www.guerrillamail.com/",
                "Mailinator": "https://www.mailinator.com/",
                "10 Minute Mail": "https://10minutemail.com/",
                "Temp Mailo": "https://temp-mailo.com/",
                "Mail Drop": "https://maildrop.cc/",
                "Fake Mail Generator": "https://www.fakemailgenerator.com/",
                "Temp Inbox": "https://www.tempinbox.com/",
                "Email On Deck": "https://emailondeck.com/",
                "Get Nada": "https://getnada.com/",
                "Sudo Mail": "https://www.sudoemail.com/",
                "Globfone": "https://globfone.com/",
                "Text EM": "https://textem.net/",
                "Receive SMS Online": "https://receive-sms-online.com/",
                "A Free SMS": "https://afreesms.com/"
            },
            "other_tools": {
                "Serial Checker": "https://github.com/masturbationnation/765-Serial-Checker",
                "Better UI Multi Tool - Coming Soon": "https://github.com/masturbationnation/MN-Multi-Tool",
                "765 CSharp Multi Tool - Coming Soon": "https://github.com/masturbationnation/765-C-Multi-Tool"
            },
            "movie_tools": {
                "Novafork": "https://novafork.com/",
                "Broflix": "https://broflix.cc",
                "Cineby": "https://www.cineby.ru/",
                "Bitcine": "https://www.bitcine.app/",
                "Freek": "https://freek.to/",
                "Hydra HD": "https://hydrahd.me/",
                "Auto Embed": "https://watch.autoembed.cc/"
            },
            "username_tools": {
                "guns.lol username checker": "https://github.com/masturbationnation/Guns-lol-Username-Checker",
                "uzi.bio username checker": "",
                "slat.cc username checker": "",
                "shock.lol username checker": "",
                "fakecrime.bio username checker": ""
            }
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_menu(self, options, header):
        self.clear_screen()
        print(ASCII_LOGO)
        print(Fore.WHITE + f"{header}\n" + "-" * len(header))
        for key, desc in options.items():
            print(Fore.WHITE + f"[{key}] {desc}")
        print()

    def get_user_choice(self, options, timeout=30):
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                print(Fore.YELLOW + "\n[Timeout] You took too long! Returning to the main menu.")
                time.sleep(2)
                return '0'
            choice = input(Fore.WHITE + "\nInput an option: ").strip()
            if choice in options:
                return choice
            print(Fore.RED + "\nInvalid input. Please try again.")

    def open_links(self, links, header, return_option="Return to Main Menu"):
        while True:
            options = {str(i + 1): desc for i, desc in enumerate(links.keys())}
            options[str(len(links) + 1)] = return_option
            self.print_menu(options, header)
            choice = self.get_user_choice(options)
            if choice == str(len(links) + 1) or choice == '0':
                return
            elif choice in options:
                webbrowser.open(list(links.values())[int(choice) - 1])

    def fake_info_menu(self):
        self.open_links(self.links["fake_info"], "Fake Info Menu")

    def edr_tools_menu(self):
        self.open_links(self.links["edr_tools"], "EDR Tools Menu")

    def osint_tools_menu(self):
        self.open_links(self.links["osint_tools"], "OSINT Tools Menu")

    def discord_tools_menu(self):
        self.open_links(self.links["discord_tools"], "Discord Tools Menu")

    def temp_tools_menu(self):
        self.open_links(self.links["temp_tools"], "Temporary Tools Menu")

    def movie_tools_menu(self):
        self.open_links(self.links["movie_tools"], "Movie/Show Tools Menu")

    def username_tools_menu(self):
        self.open_links(self.links["username_tools"], "Username Tools Menu")

    def other_tools_menu(self):
        self.open_links(self.links["other_tools"], "765's Other Tools")

    def type_message(self, message, color=Fore.WHITE, delay=0.05):
        print(color, end='')
        for char in message:
            print(char, end='', flush=True)
            time.sleep(delay)
        print(Style.RESET_ALL)

    def exit_application(self):
        self.clear_screen()
        print(ASCII_LOGO)
        self.type_message("[ Developed By ] @codacaust + @wyap on Discord")
        self.type_message("[ Support Server ] discord.gg/risking")
        time.sleep(1)
        print()
        self.type_message("[ Update v1.1 ] Added More Temp Mails & VOIP Numbers + 765 Branding")
        self.type_message("[ Current Version - Update v1.2 ] Added More Fake Info Links + Added New Section (Movies/Show Tools)")
        time.sleep(1)
        print()
        self.type_message("[ Exiting Application ] We are now closing the Multi Tool....")
        time.sleep(1)
        sys.exit(0)

    def main_menu(self):
        while True:
            self.print_menu(self.options, "Main Menu")
            choice = self.get_user_choice(self.options)
            if choice == '1':
                self.fake_info_menu()
            elif choice == '2':
                self.edr_tools_menu()
            elif choice == '3':
                self.osint_tools_menu()
            elif choice == '4':
                self.discord_tools_menu()
            elif choice == '5':
                self.temp_tools_menu()
            elif choice == '6':
                self.movie_tools_menu()
            elif choice == '7':
                self.other_tools_menu()
            elif choice == '8':
                self.username_tools_menu()
            elif choice == '9':
                self.exit_application()


if __name__ == "__main__":
    os.system("title Insidious Multi Tool")
    tool = MultiTool()
    tool.main_menu()