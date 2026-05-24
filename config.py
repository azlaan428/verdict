import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
BAND_API_KEY = os.getenv("BAND_API_KEY")
BAND_WS_URL = os.getenv("BAND_WS_URL")
BAND_REST_URL = os.getenv("BAND_REST_URL")
BAND_ROOM_ID = os.getenv("BAND_ROOM_ID")
BAND_AGENT_KEY = os.getenv("BAND_AGENT_KEY")