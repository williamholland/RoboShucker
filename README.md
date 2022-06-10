# RoboShucker

![roboshucker logo](https://github.com/williamholland/RoboShucker/blob/main/assets/robo_shucker_logo.png)

This is a small tool for using GPT3 to suggest shell commands from natural
language in the terminal.

## Setup

1. Install the python requirements

```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

2. ensure your `OPENAI_API_KEY` is defined in the environment

## Example Usage

example of calling the script:

    $ ./roboshucker.py remove all pngs in this dir more than 2 weeks

output from the above example:

    find . -mtime +14 -name "*.png" -type f -delete

## Where does the name come from?

I asked GPT3 to name this project.

## What's with the logo?

I asked Dalle-mini to design it then I traced it in inkscape
