from utils import show_banner
from utils import get_target
from utils import validate_target
from utils import resolve_target
from scanner import scan_ports
from scanner import get_port_range
from display import display_results
from colorama import init
from colors import ERROR_COLOR, RESET_COLOR, SUCCESS_COLOR
import time
from export import export_results



def main():
    init()
    
    show_banner()

    target = get_target()

    target_type = validate_target(target)

    if target_type is None:
        print(f"{ERROR_COLOR}[ERROR] Invalid target.{RESET_COLOR}")
        return
    
    resolved_ip = resolve_target(target, target_type)
    if resolved_ip is None:
        print(f"{ERROR_COLOR}[ERROR] Unable to resolve target.{RESET_COLOR}")
        return 
    
    
    start_port, end_port = get_port_range()

    start_time = time.time()
    open_ports = scan_ports(resolved_ip, start_port, end_port)
    end_time = time.time()
    scan_time = end_time - start_time
    
    display_results(target, resolved_ip, open_ports, scan_time)
    
    saved_file = export_results(target, resolved_ip, open_ports)
    print(f"{SUCCESS_COLOR}Results saved to {saved_file}{RESET_COLOR}")


if __name__ == "__main__":
    main()