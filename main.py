import os

from Data import ConstructPowerPoint
from Api import ApiRoute
from dotenv import load_dotenv

load_dotenv()
apiUrl = os.getenv("API_URL")

result = ApiRoute.call(apiUrl)
if not result.success:
    print(f"Error: {result.error}")
    exit()

data = result.data

# Construct = ConstructPowerPoint.construct()
# print("fiz", Construct)