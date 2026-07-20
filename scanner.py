import socket
from colors import SUCCESS_COLOR,ERROR_COLOR, RESET_COLOR
from concurrent.futures import ThreadPoolExecutor
from services import get_service_name

def scan_ports(resolved_ip, start_port, end_port):
    scan_results = []

    with ThreadPoolExecutor(max_workers=200) as executor:

        futures = []

        for port in range(start_port, end_port + 1):
            future = executor.submit(scan_single_port, resolved_ip, port)
            futures.append(future)

        for future in futures:
            result = future.result()

            if result is not None:
                scan_results.append({
                "port": result,
                "state": "OPEN",
                "service": get_service_name(result),
                "banner": None
            })

    return scan_results

    
def scan_single_port(resolved_ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        
        result = sock.connect_ex((resolved_ip, port))
        sock.close()
        
        if result == 0:
            return port
        
        return None



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
                
        
    
    
