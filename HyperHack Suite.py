import subprocess
import socket
import requests
import os
from colorama import Fore, Back, Style, init

# Инициализация colorama
init(autoreset=True)

# Функция для генерации ASCII-арта с градиентом
def print_ascii_art():
    ascii_art = """
    ██╗    ██╗ ██████╗  ██████╗ ██╗     ██╗   ██╗███████╗██████╗ ███████╗    ██╗  ██╗    ██╗███╗   ██╗██████╗ ██╗   ██╗███████╗████████╗██████╗ ██╗███████╗███████╗
    ██║    ██║██╔═══██╗██╔═══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔════╝    ╚██╗██╔╝    ██║████╗  ██║██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝██╔════╝
    ██║ █╗ ██║██║   ██║██║   ██║██║     ██║   ██║█████╗  ██████╔╝███████╗     ╚███╔╝     ██║██╔██╗ ██║██║  ██║██║   ██║███████╗   ██║   ██████╔╝██║█████╗  ███████╗
    ██║███╗██║██║   ██║██║   ██║██║     ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║     ██╔██╗     ██║██║╚██╗██║██║  ██║██║   ██║╚════██║   ██║   ██╔══██╗██║██╔══╝  ╚════██║
    ╚███╔███╔╝╚██████╔╝╚██████╔╝███████╗ ╚████╔╝ ███████╗██║  ██║███████║    ██╔╝ ██╗    ██║██║ ╚████║██████╔╝╚██████╔╝███████║   ██║   ██║  ██║██║███████╗███████║
     ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
    """
    
    # Разделение на строки для применения градиента
    ascii_lines = ascii_art.split("\n")
    
    # Определение начального и конечного цветов
    start_color = (0, 210, 255)  # Cyber Blue
    end_color = (138, 43, 226)   # Electric Purple
    
    # Функция для вычисления промежуточного цвета
    def get_gradient_color(start, end, factor):
        # Вычисляем промежуточные значения для RGB
        r = int(start[0] * (1 - factor) + end[0] * factor)
        g = int(start[1] * (1 - factor) + end[1] * factor)
        b = int(start[2] * (1 - factor) + end[2] * factor)
        
        # Возвращаем строку цвета для colorama
        return f"\033[38;2;{r};{g};{b}m"  # ANSI escape sequence для RGB цвета
    
    # Печать каждой строки с градиентом
    for i, line in enumerate(ascii_lines):
        # Генерация градиента для каждой строки
        factor = i / len(ascii_lines)
        color = get_gradient_color(start_color, end_color, factor)
        print(f"{color}{line}\033[0m")  # Используем ANSI escape sequence для сброса цвета

# Функция для сканирования портов
def scan_ports():
    target = input("Enter IP address to scan ports: ")
    ports = input("Enter ports to scan (comma separated): ").split(',')
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
        print(f"Open ports on {target}: {', '.join(open_ports)}")
    else:
        print(f"No open ports found on {target}.")

# Функция для трассировки маршрута
def trace_route():
    target = input("Enter IP address or domain for traceroute: ")
    try:
        # Для Windows используем tracert вместо traceroute
        command = ["tracert", target] if os.name == 'nt' else ["traceroute", target]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True, encoding='cp1251')  # Изменили кодировку на cp1251
        print(f"Traceroute to {target}:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Error performing traceroute on {target}: {e.output}")

# Функция для DNS Lookup
def dns_lookup():
    domain = input("Enter domain name for DNS lookup: ")
    try:
        output = subprocess.check_output(["nslookup", domain], stderr=subprocess.STDOUT, universal_newlines=True, encoding='cp1251')  # Изменили кодировку на cp1251
        print(f"DNS lookup for {domain}:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Error performing DNS lookup on {domain}: {e.output}")

# Функция для IP геолокации
def ip_geolocation():
    ip = input("Enter IP address for geolocation: ")
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        geolocation_data = response.json()
        print(f"Geolocation for {ip}:\n{geolocation_data}")
    except Exception as e:
        print(f"Error performing geolocation on {ip}: {e}")

# Функция для отображения меню
def display_menu():
    print("\nHyperHack Suite")
    print("1. Port Scan")
    print("2. Trace Route")
    print("3. DNS Lookup")
    print("4. IP Geolocation")
    print("5. Exit")

# Основная функция
def main():
    print_ascii_art()  # Печать ASCII-арта с градиентом
    while True:
        display_menu()
        choice = input("\nChoose an option: ")
        if choice == '1':
            scan_ports()
        elif choice == '2':
            trace_route()
        elif choice == '3':
            dns_lookup()
        elif choice == '4':
            ip_geolocation()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

# Запуск программы
if __name__ == "__main__":
    main()

