class User:
    """Represent a user on a website."""
    def __init__(self, first: str, last: str, email: str, age: int):
        """
        Create a new user.

        :param first: User's first name.
        :param last: User's last name.
        :param email: Email address associated with the user.
        :param age: User's age.
        """
        self.first = first
        self.last = last
        self.email = email
        self.age = age

    def __str__(self):
        """
        Describe the user in a string.
        (Note: for code review purposes, this is the describe user function.)

        :return: Returns a string representation of the user.
        """
        return f"{self.last}, {self.first}. Age {self.age} years old."

    def greet(self):
        """
        Greet the user (ie, when they first log in).

        :return: Return a greeting message.
        """
        return f"Hello, {self.first}!"


users = [
    User("Audrina", "Ortega", "au.ort15@gmail.com", 17),
    User("Henry", "Barcalow", "he.bar05@gmail.com", 17),
    User("Gerald", "Bruce", "ge.bru14@gmail.com", 18),
    User("Alex", "McKinstry", "al.mck26@gmail.com", 52),
    User("Tommy", "Barks", "to.bar17@gmail.com", 16),
]

for user in users:
    print(user)
    print(user.greet())
    print()

