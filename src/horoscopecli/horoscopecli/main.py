import typer
from googletrans import Translator
from horoscopeApi import getHoroscopeApi

import inputCheck

app = typer.Typer()

def translateDeco(function):
    def deco(args, **kwargs):
        typer.echo("\nBefore translation / Avant traduction:\n")
        texts = args[0]
        for text in texts:
            typer.echo(text)
        typer.echo("\n====================\n")
        translations = function(args, **kwargs)
        typer.echo("After translation / Après traduction:\n")
        for translation in translations:
            typer.echo(translation.text)
    return deco

@translateDeco
def gTranslate(text: list[str], src: str, dest: str):
    translator = Translator()
    translations = translator.translate(text, dest=dest, src=src)
    return translations

@app.command()
def getHoroscopeFromApi(sign: str = typer.Argument(..., help="The zodiac sign you want to get the horoscope of (in french or in english)"),
                        fr: bool = typer.Option(False, help="Result in french (default english)."),
                        today: bool = typer.Option(False, help="Get daily horoscope."),
                        week: bool = typer.Option(False, help="Get weekly horoscope."),
                        month: bool = typer.Option(False, help="Get monthly horoscope."),
                        year: bool = typer.Option(False, help="Get yearly horoscope.")):
    """
    This command let you check your SIGN horoscope with DATE OPTION.

    If no DATE OPTION is specified, it will give you your daily horoscope.
    """
    validSign = inputCheck.validInputSign(sign)
    if not validSign[0]:
        typer.echo(validSign[1])
        return 1
    signEn = validSign[1]
    signFr = validSign[2]

    validDateOption = inputCheck.validInputDateOption(today, week, month, year)
    if not validDateOption[0]:
        typer.echo(validDateOption[1])
        return 1

    # Api route only recognize english signs
    horoscopeEn = getHoroscopeApi(signEn, validDateOption[1])
    if fr:
        gTranslate([horoscopeEn[1]], "en", "fr")
    else:
        typer.echo(f"\nThis is your {validDateOption[2]} horoscope: ")
        typer.echo(horoscopeEn[1])
    return 0



if __name__ == "__main__":
    app()
