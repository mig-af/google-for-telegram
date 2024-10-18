from flask import Flask, request 
import asyncio
from api.Bot import Bot



TOKEN = "6607114505:AAFUnp9YWU-XMYUZ0NoPiYExC9akq3sIgpY"
obj = ""
app = Flask(__name__)   
bot = Bot(TOKEN)


def buttonResponse():
    pass



async def sendMessage(data)->None:
    busqueda = data["message"]["text"]
    boton = [
        {
            "text":"G O O G L E",
            "web_app":{"url":f"https://www.google.com/search?q={busqueda}"}
        }
    ]
    inlineButton = bot.inlineButton(boton)

    id = data["message"]["from"]["id"]
    await bot.messageSend(id, "Resultado: ", reply_markp=inlineButton)

async def startCommand(data):
    name = data["message"]["chat"]["first_name"]
    await bot.messageSend(data["message"]["from"]["id"], f"Hola {name}, \nEste bot sirve como un buscador de google\nComandos disponibles /start /creditos \nA continuacion escribe como si hicieras una busqueda en google" )
    #logging.info(f"funcion {startCommand.__name__} ejecutada con exito")


async def creditsCommand(data):
    creditos = "Creado por @pes528"
    await bot.messageSend(data["message"]["chat"]["id"], creditos)
    #logging.info(f"Funcion {creditsCommand.__name__} ejecutada")
    



@app.route("/webhook", methods=["POST", "GET"])
async def main():
    

    data = request.json
    #print(data)
    try:
        #print(data)
        data["message"]

        

        if(data["message"]["text"] == "/start"):
                
                obj = data
                await startCommand(data)
        
        elif(data["message"]["text"] == "/creditos"):
                await creditsCommand(data)
        else:
            await sendMessage(data)
           
    except KeyError:
        pass

    return "", 200


if __name__ == "__main__":

    
    app.run(port=8443, debug=True)
