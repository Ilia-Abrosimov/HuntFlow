from flow import flow

if __name__ == "__main__":
    path = input("Введите путь к папке с базой: ")
    token = input("Введите токен: ")
    print(flow(path, token))
