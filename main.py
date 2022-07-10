import typer
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = typer.Typer()

appid = os.environ['appid']


@app.command("city")
def get_city(city_name: str):

    try:
        request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}")

        response = request.json()

        typer.echo(f"{request}")
    except:
        typer.echo(f"Could not find city")


if __name__ == "__main__":
    app()
