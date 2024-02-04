import os
from subprocess import call


if __name__ == "__main__":
    print("Hello world")
    print(f"db name: {os.environ['SOURCE_DB']!r}")
    os.system("ls -lah /usr/local/bin")