import socket
import ssl


def grab_banner(target, resolved_ip, port):

    if port == 22:
        return grab_ssh_banner(resolved_ip, port)
    elif port == 80:
        return grab_http_banner(target, resolved_ip, port)
    elif port == 443:
        return grab_https_banner(target, resolved_ip, port)
    
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
    
    
    
    
def grab_http_banner(target, resolved_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)

            sock.connect((resolved_ip, port))

            request = (
                "GET / HTTP/1.1\r\n"
                f"Host: {target}\r\n"
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
    
    

def grab_https_banner(target, resolved_ip, port):
    try:
        context = ssl.create_default_context()

        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        with socket.create_connection((resolved_ip, port), timeout=2) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssl_sock:

                request = (
                    "GET / HTTP/1.1\r\n"
                    f"Host: {target}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                )

                ssl_sock.send(request.encode())

                response = ssl_sock.recv(1024).decode(errors="ignore")

                for line in response.splitlines():
                    if line.lower().startswith("server:"):
                        return line.split(":", 1)[1].strip()
                # Backup
                first_line = response.splitlines()[0]
                return first_line

                return None

    except Exception as e:
        print(e)
        return None
    
def detect_version():
    pass