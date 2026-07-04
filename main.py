from api.client import HttpClient
from api.endpoints import SERVER_TIME


def main():

    client = HttpClient()

    data = client.get(SERVER_TIME)

    print(data)


if __name__ == "__main__":
    main()