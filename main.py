from test02 import *

if __name__ == "__main__":
    city = input("Digite o nome da cidade: ")
    print(f"Temperatura em {get_weather_temp(city)}°C")
    print(f"Clima: {get_weather_main(city)}")