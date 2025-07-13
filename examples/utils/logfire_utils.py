import os

import logfire
import agents


def logfire_init():
    """
    Initialize the Logfire logger with the specified configuration.
    """
    token = os.getenv("LOGFIRE_TOKEN")
    if not token:
        print("Logfire token (envaronment variable LOGFIRE_TOKEN) not set, skipping Logfire initialization.")
        return

    logfire.configure(token=token)
    logfire.instrument_openai()
    agents.set_tracing_disabled(True)
