from utils import show_banner
from utils import get_target
from utils import validate_target


def main():
    show_banner()

    target = get_target()

    target_type = validate_target(target)

    if target_type is None:
        print("[ERROR] Invalid target.")
        return


if __name__ == "__main__":
    main()