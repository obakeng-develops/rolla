# Rolla CLI

The CLI application that allows you query weather data for cities all over the world. Built with [TyperCLI](https://typer.tiangolo.com/).

## Roadmap

- [ ] Cache weather data
- [ ] Weather forecast
- [ ] Automate weather forecast in any notification channel you want. (Email, SMS, Slack)

## Usage

To clone the project, use this command:

- `git clone https://github.com/obakeng-develops/rolla.git`

Once you have the project as a local repository, open your command-line in the project's directory and run the project in virtual environment with the below command.

For Windows:

- `.\venv\Scripts\activate.bat`

For Mac:

- `source venv/Scripts/activate.bat`

## Installation

Make sure you install all the necessary dependencies which are packaged in the `requirements.txt` file with the following command:

- `pip install -r requirements.txt`

## Authetication

The project uses [OpenWeatherMap](https://openweathermap.org) to process weather data.

Create a profile there, get your own API key and then create a `.env` file containing an `appid` variable or whatever you want to call it.

## Example

After you install dependencies, you can now run the project with this command (via TyperCLI):

- `typer main.py run Mumbai`

And you'll receive back information like below:

![rollaCLi](https://user-images.githubusercontent.com/60041842/179912932-3f55437a-be4a-45e3-8cf2-a5c5ebcce918.jpg)

You can also retrieve extra information (like country, sunrise/sunset time) with `-e` or `--extra` flag.
