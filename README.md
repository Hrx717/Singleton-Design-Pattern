# Singleton-Design-Pattern

The Singleton design pattern ensures a class has only one instance and provide a global point of access to it. 

![Singleton](https://github.com/user-attachments/assets/0efd494e-85c3-4b29-9381-5cddcf0079b6)

# Structural code in Python

```bash
class Singleton:
    _instance = None

    # Constructor is protected
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

def main():
    s1 = Singleton()
    s2 = Singleton()
    
    # Test for same instance
    if s1 is s2:
        print("Objects are the same instance")

if __name__ == "__main__":
    main()
```

# Example.py Explanation:-

Code in Example.py demonstrates the Singleton pattern as a LoadBalancing object. Only a single instance of the class can be created because servers may dynamically come on- or off-line and every request must go throught the one object that has knowledge about the state of the web servers.
