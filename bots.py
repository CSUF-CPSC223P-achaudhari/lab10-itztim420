import threading
import time

def bot_clerk(items):
    cart = []
    lock = threading.Lock()
    
    def divide_items(items):
        robot_fetchers = {1: [], 2: [], 3: []}
        for i, item in enumerate(items):
            robot_fetchers[(i % 3) + 1].append(item)
        return robot_fetchers
    
    def launch_robot_fetcher(fetcher_list):
        thread = threading.Thread(target=bot_fetcher, args=(fetcher_list, cart, lock))
        thread.start()
        return thread
    
    robot_fetchers = divide_items(items)
    threads = [launch_robot_fetcher(robot_fetchers[i]) for i in range(1, 4)]
    
    for thread in threads:
        thread.join() 
    
    return cart

def bot_fetcher(items, cart, lock):
    inventory = {
        "101": ["Notebook Paper", 2],
        "102": ["Pencils", 2],
        "103": ["Pens", 6],
        "104": ["Graph Paper", 1],
        "105": ["Paper Clips", 1],
        "106": ["Staples", 4],
        "107": ["Stapler", 7],
        "108": ["3 Ring Binder", 1],
        "109": ["Printer Paper", 1],
        "110": ["Notepad", 1]
    }

    for item_number in items:
        with lock:
            item_description, seconds = inventory[item_number]
        time.sleep(seconds)  

        with lock:
            cart.append([item_number, item_description])  