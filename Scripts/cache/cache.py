import os
import time

# CÃ³digos de escape ANSI para cores
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"

def get_cache_size():
    size_output = os.popen('du -sh $HOME/.termux/cache').read().split()[0]
    return size_output

def clear_cache():
    os.system('rm -rf $HOME/.termux/cache/*')
    print(f"{Colors.GREEN}Cache do Termux limpo.{Colors.RESET}")
    time.sleep(1)

def main():
    while True:
        print(f"{Colors.RED}CACHE CLEANER BY VINI{Colors.RESET}")
        print(f"{Colors.YELLOW}1. Exibir tamanho do cache{Colors.RESET}")
        print(f"{Colors.YELLOW}2. Limpar cache{Colors.RESET}")
        print(f"{Colors.YELLOW}3. Sair{Colors.RESET}")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            cache_size = get_cache_size()
            print(f"Tamanho do cache do Termux: {Colors.YELLOW}{cache_size}{Colors.RESET}")
            time.sleep(1)
        elif choice == '2':
            clear_cache()
        elif choice == '3':
            print(f"{Colors.YELLOW}Saindo do script. até logo!{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED} OPÇÃO ERRADA BURRO {Colors.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()