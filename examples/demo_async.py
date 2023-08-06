#!/usr/bin/env -S poetry run python

import asyncio
import os

import anthropic
from anthropic import AsyncAnthropic


async def main() -> None:
    # modified by engchina on 20230806 begin
    # client = AsyncAnthropic()
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())  # read local .env file

    client = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    # modified by engchina on 20230806 end

    res = await client.completions.create(
        model="claude-2",
        prompt=f"{anthropic.HUMAN_PROMPT} how does a court case get to the Supreme Court? {anthropic.AI_PROMPT}",
        max_tokens_to_sample=1000,
    )
    print(res.completion)


asyncio.run(main())
