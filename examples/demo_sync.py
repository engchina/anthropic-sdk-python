#!/usr/bin/env -S poetry run python
import os

import anthropic
from anthropic import Anthropic


def main() -> None:
    # modified by engchina on 20230806 begin
    # client = Anthropic()
    from dotenv import load_dotenv, find_dotenv
    _ = load_dotenv(find_dotenv())  # read local .env file

    client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    # modified by engchina on 20230806 end

    res = client.completions.create(
        model="claude-2",
        prompt=f"{anthropic.HUMAN_PROMPT} how does a court case get to the Supreme Court? {anthropic.AI_PROMPT}",
        max_tokens_to_sample=1000,
    )
    print(res.completion)


main()
