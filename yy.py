def move(self):
    if len(self) > 5:
        return "ok"
    else:
        return "no,sb"
print(move("ssssss"))