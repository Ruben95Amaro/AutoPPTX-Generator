from Api import Api_Route
from dotenv import load_dotenv
import os


def menu_endpoints(chosenEndPoint:int = None):
    print("Menu endpoints")
    if chosenEndPoint is None:
        endpointchosen = int(input("please select a endpoint: \n 1- World Cup \n 2- World Cup Standings \n 3- World Cup Matches \n"
                                   "4- Word Cup Teams"))
    else:
        endpointchosen = int(chosenEndPoint)
    result = None
    endpointUrl = None
    print(f"endpointchosen: {endpointchosen}")
    match endpointchosen:
        case 1:
            endpointUrl = "/competitions/2000"
            print("/competitions/2000")
        case 2:
            endpointUrl = "/competitions/2000/standings"
            print("/competitions/2000/standings")
        case 3:
            endpointUrl = "/competitions/2000/matches"
            print("/competitions/2000/matches")
        case 4:
            endpointUrl = "/competitions/2000/teams?season=2026"
            print("/competitions/2000/teams")


    if endpointUrl:
        result = call_competitions(endpointUrl)

    return result


def call_competitions(endpoint:str):
    load_dotenv()
    apiUrl = os.getenv("API_URL")
    if not apiUrl:
        raise Exception("No API URL provided, provide on .env please")

    # GET Api data
    worldCupUrl = apiUrl + endpoint

    # Send Post return Data
    result = Api_Route.call(str(worldCupUrl))
    return result



