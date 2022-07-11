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
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}"

        request = requests.get(url)

        print(request)

        response = request.json()

        typer.echo(f"City: {response['name']}")
        typer.echo(f"Country: {response['sys']['country']}")
        typer.echo(f"Outlook: {response['weather'][0]['main']}")
        typer.echo(f"Description: {response['weather'][0]['description']}")
    except:
        typer.echo(f"Could not find city")


if __name__ == "__main__":
    app()
