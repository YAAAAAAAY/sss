import os
import subprocess
import socket
import requests
import os
import time
from colorama import Fore, Back, Style, init
from itertools import cycle

# Устанавливаем размер окна консоли на 170 колонок и 50 строк
os.system('mode con: cols=170 lines=50')

init(autoreset=True)

def print_ascii_art():
    ascii_art = """
    ██╗    ██╗ ██████╗  ██████╗ ██╗     ██╗   ██╗███████╗██████╗ ███████╗    ██╗  ██╗    ██╗███╗   ██╗██████╗ ██╗   ██╗███████╗████████╗██████╗ ██╗███████╗███████╗
    ██║    ██║██╔═══██╗██╔═══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔════╝    ╚██╗██╔╝    ██║████╗  ██║██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝██╔════╝
    ██║ █╗ ██║██║   ██║██║   ██║██║     ██║   ██║█████╗  ██████╔╝███████╗     ╚███╔╝     ██║██╔██╗ ██║██║  ██║██║   ██║███████╗   ██║   ██████╔╝██║█████╗  ███████╗
    ██║███╗██║██║   ██║██║   ██║██║     ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║     ██╔██╗     ██║██║╚██╗██║██║  ██║██║   ██║╚════██║   ██║   ██╔══██╗██║██╔══╝  ╚════██║
    ╚███╔███╔╝╚██████╔╝╚██████╔╝███████╗ ╚████╔╝ ███████╗██║  ██║███████║    ██╔╝ ██╗    ██║██║ ╚████║██████╔╝╚██████╔╝███████║   ██║   ██║  ██║██║███████╗███████║
     ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝  
    """

    ascii_lines = ascii_art.split("\n")
    start_color = (0, 210, 255)
    end_color = (138, 43, 226)

    def get_gradient_color(start, end, factor):
        r = int(start[0] * (1 - factor) + end[0] * factor)
        g = int(start[1] * (1 - factor) + end[1] * factor)
        b = int(start[2] * (1 - factor) + end[2] * factor)
        return f"\033[38;2;{r};{g};{b}m"

    for i, line in enumerate(ascii_lines):
        factor = i / len(ascii_lines)
        color = get_gradient_color(start_color, end_color, factor)
        print(f"{color}{line}\033[0m")

def scan_ports():
    target = input(f"\n{Fore.CYAN}Enter IP address to scan ports: {Style.RESET_ALL}")
    ports = input(f"{Fore.CYAN}Enter ports to scan (comma separated): {Style.RESET_ALL}").split(',')
    open_ports = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, int(port)))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            pass

    if open_ports:
        print(f"{Fore.GREEN}\nOpen ports on {target}: {', '.join(open_ports)}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}\nNo open ports found on {target}.{Style.RESET_ALL}")

def trace_route():
    target = input(f"\n{Fore.CYAN}Enter IP address or domain for traceroute: {Style.RESET_ALL}")
    try:
        command = ["tracert", target] if os.name == 'nt' else ["traceroute", target]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True, encoding='cp1251')
        print(f"\n{Fore.MAGENTA}Traceroute to {target}:\n{output}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}\nError performing traceroute on {target}: {e.output}{Style.RESET_ALL}")

def dns_lookup():
    domain = input(f"\n{Fore.CYAN}Enter domain name for DNS lookup: {Style.RESET_ALL}")
    try:
        output = subprocess.check_output(["nslookup", domain], stderr=subprocess.STDOUT, universal_newlines=True, encoding='cp1251')
        print(f"\n{Fore.BLUE}DNS lookup for {domain}:\n{output}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}\nError performing DNS lookup on {domain}: {e.output}{Style.RESET_ALL}")

def ip_geolocation():
    ip = input(f"\n{Fore.CYAN}Enter IP address for geolocation: {Style.RESET_ALL}")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        geolocation_data = response.json()
        print(f"\n{Fore.GREEN}Geolocation for {ip}:\n{geolocation_data}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}\nError performing geolocation on {ip}: {e}{Style.RESET_ALL}")

def loading_animation():
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}Loading...{Style.RESET_ALL}")
    spinner = cycle(['|', '/', '-', '\\'])
    for _ in range(20):
        print(f"\r{next(spinner)}", end='', flush=True)
        time.sleep(0.1)
    print("\rDone!")

def console_access():
    print(f"\n{Fore.CYAN}Opening console...{Style.RESET_ALL}")
    while True:
        command = input(f"{Fore.YELLOW}HyperHack> {Style.RESET_ALL}")
        if command.lower() == "exit":
            break
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
            print(f"{Fore.GREEN}{output}{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error executing command: {e.output}{Style.RESET_ALL}")

def display_menu():
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}╔════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}║            HyperHack Suite             ║{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}╚════════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. Port Scan{Style.RESET_ALL}")
    print(f"{Fore.CYAN}2. Trace Route{Style.RESET_ALL}")
    print(f"{Fore.CYAN}3. DNS Lookup{Style.RESET_ALL}")
    print(f"{Fore.CYAN}4. IP Geolocation{Style.RESET_ALL}")
    print(f"{Fore.CYAN}5. Open Console{Style.RESET_ALL}")
    print(f"{Fore.RED}6. Exit{Style.RESET_ALL}")

def main():
    print_ascii_art()
    while True:
        display_menu()
        choice = input(f"\n{Fore.CYAN}Choose an option: {Style.RESET_ALL}")
        if choice == '1':
            loading_animation()
            scan_ports()
        elif choice == '2':
            loading_animation()
            trace_route()
        elif choice == '3':
            loading_animation()
            dns_lookup()
        elif choice == '4':
            loading_animation()
            ip_geolocation()
        elif choice == '5':
            console_access()
        elif choice == '6':
            print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice, please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
