from utils import show_banner
from utils import get_target
from utils import validate_target
from utils import resolve_target


def main():
    show_banner()

    target = get_target()

    target_type = validate_target(target)

    if target_type is None:
        print("[ERROR] Invalid target.")
        return
    
    resolved_ip = resolve_target(target, target_type)
    print("ip:", resolved_ip)
    if resolved_ip is None:
        print("[ERROR] Unable to resolve target.")
        return 


if __name__ == "__main__":
    main()