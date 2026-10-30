import socket


def dns_res(value: str) -> str:
    try:
        hostname, aliales, address = socket.gethostbyaddr(value)
        return hostname

    except socket.herror as err:
        return "UKNOWN-DNS"
    except Exception as err:
        return "Произошла неожиданная ошибка: {err}"





