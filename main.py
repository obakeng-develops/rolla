from datetime import datetime
import typer
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = typer.Typer()

appid = os.environ['appid']


@app.command("city")
def get_city(city_name: str, extra: bool = typer.Option(None, "--extra", "-e", help="Get extra information about the city")):

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}&units=metric"

        request = requests.get(url)

        response = request.json()

        sunrise = datetime.fromtimestamp(response['sys']['sunrise'])
        sunset = datetime.fromtimestamp(response['sys']['sunset'])
        temp = response['main']['temp']

        if extra:
            typer.echo(f"City: {response['name']}")
            typer.echo(f"Temperature: {temp}")
            typer.echo(f"Country: {response['sys']['country']}")
            typer.echo(f"Outlook: {response['weather'][0]['main']}")
            typer.echo(f"Description: {response['weather'][0]['description']}")
            typer.echo(f"Sunrise: {sunrise}")
            typer.echo(f"Sunset: {sunset}")
        else:
            typer.echo(f"City: {response['name']}")
            typer.echo(f"Temperature: {temp}")
            typer.echo(f"Outlook: {response['weather'][0]['main']}")
            typer.echo(f"Description: {response['weather'][0]['description']}")
    except:
        typer.echo(f"Could not find city")


if __name__ == "__main__":
    app()
