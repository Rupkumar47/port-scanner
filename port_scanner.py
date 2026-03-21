import socket

def scan_ports(target, start_port=1, end_port=100):
    print("=" * 50)
    print(f"Scanning Target: {target}")
    print(f"Port Range: {start_port} - {end_port}")
    print("=" * 50)

    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)

            sock.close()

    except KeyboardInterrupt:
        print("\n Scan interrupted by user")
        return
    except socket.gaierror:
        print("\n Hostname could not be resolved")
        return
    except socket.error:
        print("\n Could not connect to server")
        return

    print("\n" + "=" * 50)
    print("Scan Completed")

    if open_ports:
        print(f" Open Ports: {open_ports}")
    else:
        print(" No open ports found")

    print("=" * 50)


if __name__ == "__main__":
    target = input("Enter target (IP or domain): ")
    scan_ports(target)
