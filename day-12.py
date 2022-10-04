enemies = 1


def increase_enemies():
    # global enemies
    # enemies += 2
    print(f"enemies inside function: {enemies}")
    return enemies + 2


increase_enemies()
print(f"enemies outside function: {enemies}")
