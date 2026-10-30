from module.scan.agressive_scan import run_scan

import sys
import argparse
import ipaddress as ipaddr


flag_parser = argparse.ArgumentParser(description="netscan v-1.5.2 by https://github.com/noxveil-xy")
add_flag_siA = flag_parser.add_argument('-siA', type=str, required=False, help='Агрессивный APR-SCAN.')
args = flag_parser.parse_args()


if __name__ == "__main__":
    try:
        if args.siA != "":

            ip_net = ipaddr.ip_network(args.siA)

            print(f"\nСканирование..\n")
            run_scan(args.siA)

    except ValueError:
        print(f"\nОшибка: нужно передать адрес сети или хоста.\n")
    except Exception as err:
        print(f"Произошла неожиданая ошибка: {err}")

