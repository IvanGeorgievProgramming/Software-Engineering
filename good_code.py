class PrettyPrinter:
    """Class to demonstrate pretty Python code according to PEP 8."""

    def __init__(self, message):
        self.message = message

    def print_message(self):
        """Prints a formatted message."""
        print(f"Message: {self.message}")

    def print_divider(self, length=40, char='*'):
        """Prints a divider line with a customizable character and length."""
        print(char * length)


if __name__ == '__main__':
    # Create an instance of PrettyPrinter
    pretty = PrettyPrinter("Hello, PEP 8!")

    # Call the methods of the PrettyPrinter class
    pretty.print_message()
    pretty.print_divider()
    pretty.print_divider(length=60, char='-')
