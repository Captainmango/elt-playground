import os


if __name__ == "__main__":
    print("Hello world")
    print(f"db name: {os.environ['SOURCE_DB']!r}")