
import socket
from static_log_file_forwarder.config import conf


def send_to_logger(data):
    host = conf.read().get('prod-logger-input', 'host')
    port = conf.read().get('prod-logger-input', 'port')
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc.sendto(bytes(data, encoding='utf-8'), (host, int(port)))


def main():
    count = 0
    path = conf.read().get('log-file', 'path')
    with open(path, 'r') as log_file:
        for line in log_file:
            print(line)
            send_to_logger(line)
    print(count)


if __name__ == '__main__':
    main()