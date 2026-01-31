import os
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# Combined hardcoded city data (temperature and local sunrise/sunset)
_CITY_DATA = {
    "new york": {"min": -1, "max": 5, "sunrise": "07:00", "sunset": "17:20"},
    "london": {"min": 2, "max": 8, "sunrise": "07:40", "sunset": "16:55"},
    "paris": {"min": 3, "max": 9, "sunrise": "08:05", "sunset": "17:10"},
    "tokyo": {"min": 6, "max": 13, "sunrise": "06:30", "sunset": "17:15"},
    "sydney": {"min": 15, "max": 23, "sunrise": "06:10", "sunset": "18:00"},
    "mumbai": {"min": 24, "max": 32, "sunrise": "06:55", "sunset": "18:25"},
    "dubai": {"min": 18, "max": 28, "sunrise": "06:50", "sunset": "18:15"},
    "beijing": {"min": -3, "max": 4, "sunrise": "07:20", "sunset": "17:45"},
    "moscow": {"min": -10, "max": -2, "sunrise": "09:15", "sunset": "17:10"},
    "new delhi": {"min": 2, "max": 6, "sunrise": "07:20", "sunset": "18:05"},
}


def getTemperature(city: str):
	"""Return today's min and max temperature for the given city.
	City matching is case-insensitive. Returns a dict with keys 'min' and 'max'.
	Raises ValueError if city not in the hardcoded list.
	"""
	if not isinstance(city, str) or not city.strip():
		raise ValueError("city must be a non-empty string")
	key = city.strip().lower()
	if key not in _CITY_DATA:
		return(f"City '{city}' not in the list.")
	entry = _CITY_DATA[key]
	return {"min": entry["min"], "max": entry["max"]}


def sunrise_sunset(city: str):
	"""Return local sunrise and sunset times for the given city.
	City matching is case-insensitive. Returns a dict with keys 'sunrise' and 'sunset'.
	Raises ValueError if city not in the hardcoded list.
	"""
	if not isinstance(city, str) or not city.strip():
		raise ValueError("city must be a non-empty string")
	key = city.strip().lower()
	if key not in _CITY_DATA:
		return(f"City '{city}' not in the list.")
	entry = _CITY_DATA[key]
	return {"sunrise": entry["sunrise"], "sunset": entry["sunset"]}


'''if __name__ == "__main__":
	# quick demo showing temperature and sunrise/sunset from a single data source
	for name in ["New York", "London", "Tokyo", "New Delhi", "Unknown City"]:
		try:
			temps = getTemperature(name)
			sun = sunrise_sunset(name)
			print(f"{name}: min={temps['min']}°C, max={temps['max']}°C, sunrise={sun['sunrise']}, sunset={sun['sunset']}")
		except ValueError as e:
			print(e)'''


agent=create_agent(
	model="gpt-4o-mini",
	tools=[getTemperature, sunrise_sunset],
	system_prompt="""You are an AI assistant. User can ask you question about a city or a place in city.
	Instead of giving the name of city directly, user may provide the name of a famous place or monument in the city, find out city name. 
	If you have a city name, invoke necessary tool to answer, else respond that you cannot locate the place. 
	If you have the city name but tool cannot find the details of that city, then apologize and reply 
	that you do not have the necessary details for the city to answer the question"""
)
response=agent.invoke({"messages":[{"role":"user", "content":"When will the last glimpse of sun be seen from Victoria Memorial? What kind of garments I need to carry if I want to see watch from Victoria Memorial"}]})
print(response["messages"])