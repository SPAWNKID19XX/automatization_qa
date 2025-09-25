class User:
    def __init__(self, name: str = None, email: str = None, age: int = None):
        self.name = name
        self.email = email

        if age is not None:
            if isinstance(age,str):
                s=age.strip()

                if s.isdigit():
                    age = int(s)

                else:
                    raise TypeError("Age should be Int")

            if not isinstance(age, int):
                raise TypeError("Age should be Int")

            if age < 1 or age > 100:
                raise ValueError("Age should be between 1..100")
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age} {self.email}"

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age