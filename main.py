import typer

app = typer.Typer()

@app.command("city")
def get_city():
    typer.echo("Hello")

if __name__ == "__main__":
    app()