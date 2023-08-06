#!/usr/bin/env -S poetry run python

import asyncio
import os

from anthropic import Anthropic, AsyncAnthropic


def sync_tokens() -> None:
    # modified by engchina on 20230806 begin
    #  client = Anthropic()
    from dotenv import load_dotenv, find_dotenv

    _ = load_dotenv(find_dotenv())  # read local .env file

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    # modified by engchina on 20230806 end

    text = "hello world!"

    tokens = client.count_tokens(text)
    print(f"'{text}' is {tokens} tokens")

    assert tokens == 3


async def async_tokens() -> None:
    # modified by engchina on 20230806 begin
    #  anthropic = AsyncAnthropic()
    from dotenv import load_dotenv, find_dotenv

    _ = load_dotenv(find_dotenv())  # read local .env file

    anthropic = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    # modified by engchina on 20230806 end

    text = "fist message"
    tokens = await anthropic.count_tokens(text)
    print(f"'{text}' is {tokens} tokens")

    text = "second message"
    tokens = await anthropic.count_tokens(text)
    print(f"'{text}' is {tokens} tokens")


sync_tokens()
asyncio.run(async_tokens())
