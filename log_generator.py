"""This script generates log messages using the OpenAI API and writes them to a file."""
import os
import random
import time
import sys
from openai import OpenAI

def get_log_text():
    """Fetch log messages from the OpenAI API and write them to a file."""
    print("Fetching log messages from OpenAI API...", flush=True)
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
    )

    response = client.responses.create(
        input="Create 10 log messages from one of the type INFO, WARNING, ERROR, DEBUG, CRITICAL, EXCEPTION, ALERT, EMERGENCY. Keep it concise and relevant to software development. Do not write anything else other than the log messages. Do not include any explanations or additional text. Just the log messages in the specified format. Keep them short and to the point. Keep all the messages in a single response, separated by newlines and under 500 tokens. Keep the language english only. Use the format and only this format =  [timestamp] [log_type]: [message].",
        model="allam-2-7b",
    )
    return(response.output_text)

def main():
    """Main function to generate logs and sleep for a random interval."""
    print("Generating logs...", flush=True)
    print(get_log_text(), flush=True)
    sleep_time = random.uniform(10, 30)
    time.sleep(sleep_time)

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Logger stopped by user.")
        sys.exit(0)
