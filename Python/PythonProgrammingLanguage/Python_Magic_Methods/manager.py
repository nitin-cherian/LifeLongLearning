# manager.py


class Manager:
    def __enter__(self):
        print("Entering")
        return "some value"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting')
        print(exc_type, exc_val, exc_tb)

