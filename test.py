


def example_func(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


data = {"name":"tom","age":36,"city":"LA"}

example_func(**data)
