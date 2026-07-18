from utils import show_banner
from utils import get_target
from utils import validate_target
from utils import resolve_target
from scanner import scan_ports
from scanner import get_port_range
from display import display_results



def main():
    show_banner()

    target = get_target()

    target_type = validate_target(target)

    if target_type is None:
        print("[ERROR] Invalid target.")
        return
    
    resolved_ip = resolve_target(target, target_type)
    if resolved_ip is None:
        print("[ERROR] Unable to resolve target.")
        return 
    
    start_port, end_port = get_port_range()

    open_ports = scan_ports(resolved_ip, start_port, end_port)

    display_results(target, resolved_ip, open_ports)


if __name__ == "__main__":
    main()