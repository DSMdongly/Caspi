from caspi import cu, gs25, seven_eleven
import json

if __name__ == '__main__':
    print(json.dumps(seven_eleven.get_plus_event_products(), ensure_ascii=False, indent=2))