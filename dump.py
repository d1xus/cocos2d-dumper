import subprocess
import sys
import os
import re
import time
from collections import defaultdict

def FNytsNtZ(SNGvlyQd, FkYotrqi):
    return f'\x1b[{FkYotrqi}m{SNGvlyQd}\x1b[0m'
MESSAGES = {'en': {'banner': "\n   ____  _  __           \n  |  _ \\(_)/ _| ___ _ __ \n  | | | | | |_ / _ \\ '__|\n  | |_| | |  _|  __/ |   \n  |____/|_|_|  \\___|_|   \n    DUMPER BY D1XUS      \n   Thanks to Lewis       \n", 'install_termux': '[*] Installing binutils via pkg...', 'install_linux': '[*] Installing binutils via apt-get...', 'extracting': '[*] Extracting symbols from', 'generating_dump': '[*] Generating method dump...', 'saved_to': '[✓] Dump saved to', 'usage': 'Usage: python3 dump.py <lib.so> [en|ru]', 'file_not_found': 'File not found:', 'termux_detected': '[*] Termux environment detected', 'linux_detected': '[*] Linux system detected', 'grant_storage': '[!] Make sure you ran: termux-setup-storage'}, 'ru': {'banner': "\n   ____  _  __           \n  |  _ \\(_)/ _| ___ _ __ \n  | | | | | |_ / _ \\ '__|\n  | |_| | |  _|  __/ |   \n  |____/|_|_|  \\___|_|   \n    DUMPER BY D1XUS      \n   Спасибо Lewis         \n", 'install_termux': '[*] Установка binutils через pkg...', 'install_linux': '[*] Установка binutils через apt-get...', 'extracting': '[*] Извлечение символов из', 'generating_dump': '[*] Генерация дампа методов...', 'saved_to': '[✓] Дамп сохранён в', 'usage': 'Использование: python3 dump.py путь_к_файлу.so [en|ru]', 'file_not_found': 'Файл не найден:', 'termux_detected': '[*] Обнаружено окружение Termux', 'linux_detected': '[*] Обнаружена система Linux', 'grant_storage': '[!] Убедись, что ты дал доступ к хранилищу: termux-setup-storage'}}

def kEZidLxJ(oUCPjjNs):
    print(FNytsNtZ(MESSAGES[oUCPjjNs]['banner'], '95'))

def apozkraz():
    prefix = os.environ.get('PREFIX', '')
    if 'com.termux' in prefix:
        return True
    return subprocess.run(['which', 'pkg'], stdout=subprocess.DEVNULL).returncode == 0

def RmdtiZRG(xVhyUtpZ):
    return subprocess.run(['which', xVhyUtpZ], stdout=subprocess.DEVNULL).returncode == 0

def eLPkYBIb(oUCPjjNs):
    print(FNytsNtZ(MESSAGES[oUCPjjNs]['install_termux'], '94'))
    subprocess.run(['pkg', 'update', '-y'])
    subprocess.run(['pkg', 'install', 'binutils', '-y'])

def ddskMgPY(oUCPjjNs):
    print(FNytsNtZ(MESSAGES[oUCPjjNs]['install_linux'], '94'))
    subprocess.run(['sudo', 'apt-get', 'update', '-y'])
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'binutils'])

def nHkVKptL(kgsGqkXV, oUCPjjNs, TVKuydWt='symbolsDec.txt'):
    print(FNytsNtZ(f"{MESSAGES[oUCPjjNs]['extracting']} {kgsGqkXV}...", '93'))
    with open(TVKuydWt, 'w', encoding='utf-8') as f_out:
        p1 = subprocess.Popen(['readelf', '-Ws', kgsGqkXV], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(['c++filt'], stdin=p1.stdout, stdout=f_out)
        p1.stdout.close()
        p2.communicate()

def pspxmHaJ(oUCPjjNs, UeNwppAX='symbolsDec.txt', XYRrhZOb='output/dump.cs'):
    classes = defaultdict(list)
    pattern = re.compile('^\\s*\\d+:\\s+([0-9a-fA-F]{8})\\s+\\d+\\s+FUNC\\s+GLOBAL.*?\\s+([a-zA-Z0-9_:~]+::[a-zA-Z0-9_~]+\\([^)]*\\))')
    with open(UeNwppAX, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(FNytsNtZ(MESSAGES[oUCPjjNs]['generating_dump'], '92'))
    total = len(lines)
    done = 0
    for line in lines:
        match = pattern.search(line)
        if match:
            offset, full_name = match.groups()
            if offset == '00000000':
                continue
            if '::' in full_name:
                class_path, method_with_params = full_name.rsplit('::', 1)
                method_name = method_with_params.split('(')[0]
                params = method_with_params[len(method_name):]
                classes[class_path].append((method_name, params, offset))
        done += 1
        if done % 50 == 0:
            zpOrbpmP(done, total)
    os.makedirs(os.path.dirname(XYRrhZOb), exist_ok=True)
    with open(XYRrhZOb, 'w', encoding='utf-8') as out:
        for cls in sorted(classes):
            out.write(f'class {cls} {{\n')
            for method_name, params, offset in sorted(set(classes[cls])):
                out.write(f'    // offset: 0x{offset}\n')
                out.write(f'    void {method_name}{params};\n')
            out.write('};\n\n')
    print()
    print(FNytsNtZ(f"{MESSAGES[oUCPjjNs]['saved_to']} {XYRrhZOb}", '92'))

def zpOrbpmP(wlTSDMIE, wiyVietu, UonjzaFd=30):
    percent = wlTSDMIE / wiyVietu
    filled = int(UonjzaFd * percent)
    bar = FNytsNtZ('█' * filled, '96') + '-' * (UonjzaFd - filled)
    print(f'\r[{bar}] {int(percent * 100)}%', end='', flush=True)
    time.sleep(0.01)

def yVJvwZwX():
    subprocess.run(['clear'])
    oUCPjjNs = 'ru'
    if len(sys.argv) == 3 and sys.argv[2] in ('ru', 'en'):
        oUCPjjNs = sys.argv[2]
    kEZidLxJ(oUCPjjNs)
    if len(sys.argv) < 2:
        print(FNytsNtZ(MESSAGES[oUCPjjNs]['usage'], '91'))
        sys.exit(1)
    kgsGqkXV = sys.argv[1]
    if not os.path.isfile(kgsGqkXV):
        print(FNytsNtZ(f"{MESSAGES[oUCPjjNs]['file_not_found']} {kgsGqkXV}", '91'))
        sys.exit(1)
    termux = apozkraz()
    if termux:
        print(FNytsNtZ(MESSAGES[oUCPjjNs]['termux_detected'], '94'))
        if not RmdtiZRG('readelf') or not RmdtiZRG('c++filt'):
            eLPkYBIb(oUCPjjNs)
        print(FNytsNtZ(MESSAGES[oUCPjjNs]['grant_storage'], '93'))
    else:
        print(FNytsNtZ(MESSAGES[oUCPjjNs]['linux_detected'], '94'))
        if not RmdtiZRG('readelf') or not RmdtiZRG('c++filt'):
            ddskMgPY(oUCPjjNs)
    nHkVKptL(kgsGqkXV, oUCPjjNs)
    pspxmHaJ(oUCPjjNs)
if __name__ == '__main__':
    yVJvwZwX()