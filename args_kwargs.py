#Santiago Pineda, *args **kwargs 

def hello(name, *args):
    for first in args:
        print(f"Hello {first}{name}")

hello(" Fate",  "Sol", "Cash", "Chip", "Al", "Dhalia", "Penelop", "Helen") 

hello("Kringle", "Kris")

def clean(data, decimals=0,**kwargs):
    if not kwargs.get("data"):
        return "There is no data"
    elif kwargs.get("type") == "str":
        return data.strip().lower()
    elif kwargs.get("types") == "int":
        return int(data)
    elif kwargs.get("type") == "float":
        if kwargs.get("decimals"):
            decimals = kwargs.get(decimals)
        return round(float(data), kwargs["decimals"])
    elif kwargs.get("type") == "list":
        return str(f"{x}, " for x in data)
    elif kwargs.get("type") == "bool":
        return f"{data}"
    else:
        return "No data type given"
print(clean("Utah", type="str"))
print(clean([1,2,3]), type="list")