import socket
from colors import SUCCESS_COLOR,ERROR_COLOR, RESET_COLOR
def scan_ports(resolved_ip, start_port, end_port):
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((resolved_ip, port))
        
        if result == 0:
            open_ports.append(port)
        
        sock.close()
            
    return open_ports



def get_port_range():
    while True:
        try:
            start_port = int(input("Start port: ").strip())
        except ValueError:
            print(f"{ERROR_COLOR}[ERROR] Port must be a number.\n{RESET_COLOR}")
            continue

        if not (1 <= start_port <= 65535):
            print(f"{ERROR_COLOR}[ERROR] Out of range.\n{RESET_COLOR}")
            continue

        while True:
            try:
                end_port = int(input("End port: ").strip())
            except ValueError:
                print(f"{ERROR_COLOR}[ERROR] Port must be a number.\n{RESET_COLOR}")
                continue

            if not (1 <= end_port <= 65535):
                print(f"{ERROR_COLOR}[ERROR] Out of range.\n{RESET_COLOR}")
                continue

            if start_port > end_port:
                print(f"{ERROR_COLOR}[ERROR] Start port cannot be greater than end port.\n{RESET_COLOR}")
                break

            return start_port, end_port
                
        
    
    
