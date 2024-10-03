import random
import threading

class LoadBalancer:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(LoadBalancer, cls).__new__(cls)
                    cls._instance.servers = [
                        "ServerI",
                        "ServerII",
                        "ServerIII",
                        "ServerIV",
                        "ServerV"
                    ]
                    cls._instance.random = random.Random()
        return cls._instance

    @property
    def server(self):
        return self.random.choice(self.servers)

def main():
    b1 = LoadBalancer()
    b2 = LoadBalancer()
    b3 = LoadBalancer()
    b4 = LoadBalancer()

    # Same instance?
    if b1 is b2 and b2 is b3 and b3 is b4:
        print("Same instance\n")

    # Load balance 15 server requests
    balancer = LoadBalancer()
    for _ in range(15):
        server = balancer.server
        print(f"Dispatch Request to: {server}")

if __name__ == "__main__":
    main()
