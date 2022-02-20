from pipfile import Pipfile


def build_package(key, value):
    if "extras" in value:
        new_val = value["extras"][0]
        return f"{key}[{new_val}]\n"
    if "*" in value:
        return f"{key}==*\n"
    return f"{key}{value}\n"


parsed = Pipfile.load(filename="Pipfile")
package = parsed.data.get("default")
value = "".join([build_package(key, value) for (key, value) in package.items()])

with open("requirements.txt", "w") as file:
    file.write(value + "pytest==7.0.1\n" + "requests==2.27.1\n")
