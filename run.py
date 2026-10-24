from module.scan.agressive_scan import run_scan
import sys

if __name__ == "__main__":
    try:
        if sys.argv[1] == None:
            print(f"Ошибка: нужно указать CIDR.")
        else:
            print(f"\nСканирование..\n")
            run_scan(sys.argv[1])


    except Exception as err:
        print(f"Произошла неожиданая ошибка: {err}")

