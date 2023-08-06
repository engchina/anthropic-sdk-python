#!/usr/bin/env -S poetry run python

import asyncio
import os

from anthropic import AI_PROMPT, HUMAN_PROMPT, Anthropic, APIStatusError, AsyncAnthropic

# modified by engchina on 20230806 begin
# client = Anthropic()
# async_client = AsyncAnthropic()
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
async_client = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
# modified by engchina on 20230806 end

question = """
Hey Claude! How can I recursively list all files in a directory in Python?
"""


def sync_stream() -> None:
    stream = client.completions.create(
        prompt=f"{HUMAN_PROMPT} {question}{AI_PROMPT}",
        model="claude-2",
        stream=True,
        max_tokens_to_sample=300,
    )

    for completion in stream:
        print(completion.completion, end="")

    print()


async def async_stream() -> None:
    stream = await async_client.completions.create(
        prompt=f"{HUMAN_PROMPT} {question}{AI_PROMPT}",
        model="claude-2",
        stream=True,
        max_tokens_to_sample=300,
    )

    async for completion in stream:
        print(completion.completion, end="")

    print()


def stream_error() -> None:
    try:
        client.completions.create(
            prompt=f"{HUMAN_PROMPT}{question}{AI_PROMPT}",
            model="claude-unknown-model",
            stream=True,
            max_tokens_to_sample=300,
        )
    except APIStatusError as err:
        print(f"Caught API status error with response body: {err.response.text}")


sync_stream()
asyncio.run(async_stream())
stream_error()
