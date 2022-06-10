#!/usr/bin/env python3

import os
import sys
import openai
import argparse


# this is passed to GPT3 as an example of how to respond
prompt_example = """\
[Prompt] a bash command to print \"hello world\":
[Response] echo \"hello world\"
"""

parser = argparse.ArgumentParser()
parser.add_argument('prompt', nargs=argparse.REMAINDER)
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-m', '--model',
    default='text-davinci-002',
    choices=[
        'text-davinci-002',
        'text-curie-001',
        'text-babbage-001',
        'text-ada-001',
    ],
    help='GPT model to use. From experience only davinci seems to work well'
)
args = parser.parse_args(sys.argv[1:])

openai.api_key = os.getenv("OPENAI_API_KEY")

formatted_input = ' '.join(args.prompt)
prompt = prompt_example + f'[Prompt] a bash command to {formatted_input}\n[Response]'
completion_kwargs = {
    'model': args.model,
    'prompt': prompt,
    'temperature': 0.7,
    'max_tokens': 64,
    'top_p': 1,
    'frequency_penalty': 0,
    'presence_penalty': 0,
    'stop': ["[Prompt]"]
}
if args.verbose:
    print('calling openai completion create with:')
    print(completion_kwargs)

response = openai.Completion.create(**completion_kwargs)

if args.verbose:
    print('response from openai:')
    print(response)

print(response['choices'][0]['text'].strip())
