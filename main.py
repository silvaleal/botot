import typer

from botot import Botot

app = typer.Typer()

@app.command()
def version():
    print(f"v0-prototype")

    
@app.command()
def run(phpproject, title:str="My first app", port:int=3011):
    botot = Botot()
    botot.create_app(title, port, phpproject)

    botot.run()

if __name__ == "__main__":
    app()