import socket

def grab_banner(resolved_ip, port):

    if port == 22:
        return grab_ssh_banner(resolved_ip, port)
    elif port == 80:
        return grab_http_banner(resolved_ip, port)
    
    return None


def grab_ssh_banner(resolved_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)

            sock.connect((resolved_ip, port))

            banner = sock.recv(1024).decode(errors="ignore").strip()

            return banner

    except (socket.timeout, ConnectionResetError, OSError):
        return None
    
    
    
    
def grab_http_banner(resolved_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)

            sock.connect((resolved_ip, port))

            request = (
                "GET / HTTP/1.1\r\n"
                f"Host: {resolved_ip}\r\n"
                "Connection: close\r\n"
                "\r\n"
            )

            sock.send(request.encode())

            response = sock.recv(1024).decode(errors="ignore")

            for line in response.splitlines():
                if line.lower().startswith("server:"):
                    return line.replace("Server:", "").strip()

            return None

    except (socket.timeout, ConnectionResetError, OSError):
        return None
    
def detect_version():
    pass