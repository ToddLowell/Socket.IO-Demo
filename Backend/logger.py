def log(msg, clr="purple"):
    # https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences
    colors = {
        "purple": "\033[95m",
        "blue": "\033[94m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
    }

    try:
        colors[clr]
    except KeyError:
        clr = "purple"

    return f"{colors[clr]}{msg}\033[0m"