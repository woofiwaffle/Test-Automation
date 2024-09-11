import socket
import threading


def scan_port(host, port, result):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result[port] = sock.connect_ex((host, port)) == 0
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    finally:
        sock.close()


def scan_ports(host, ports):
    threads = []
    result = {}
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    open_ports = [port for port, is_open in result.items() if is_open]
    return open_ports


if __name__ == "__main__":
    target_host = "opensource-demo.orangehrmlive.com"
    port_range = range(1, 1025)
    open_ports = scan_ports(target_host, port_range)
    print(f"Open ports: {open_ports}")