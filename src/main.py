from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
from test import test_utils

def main():
    print("HI")
    return 0

if __name__ == "__main__":
    main()