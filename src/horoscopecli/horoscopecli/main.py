import typer
from googletrans import Translator

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

if __name__ == "__main__":
    app()
