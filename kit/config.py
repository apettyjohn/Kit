from os import getenv
from pathlib import Path
from dotenv import load_dotenv
from kit.paths import CONTEXT_DIR

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------
load_dotenv()
TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", "")

KIT_CONTEXT_DIR = Path(getenv("KIT_CONTEXT_DIR") or str(CONTEXT_DIR))

KIT_MODEL = getenv("KIT_MODEL", "x-ai/grok-4.1-fast")
