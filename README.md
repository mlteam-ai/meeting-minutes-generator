# Meeting Minutes Generator

# Overview
In this tutorial, we'll harness the power of OpenAI's Whisper and GPT-4 models to develop an automated meeting minutes generator. The application transcribes audio from a meeting, provides a summary of the discussion, extracts key points and action items, and performs a sentiment analysis. You can find the full tutorial in the [OpenAI documentation](https://platform.openai.com/docs/tutorials/meeting-minutes). 

# Installation
This project is tested in Python 3.12.1 and openai python libarary 1.9.0.

## 1. Setting up the '.env' file
You need to subscribe to [OpenAI](https://platform.openai.com/docs/quickstart/account-setup), configure your [billing settings](https://platform.openai.com/account/billing/overview), get your API key and create an '.env' file containing 'OPENAI_API_KEY'.

Here is a sample '.env' file:
```
OPENAI_API_KEY=12345
```

## 2. Installing the dependencies
Open a terminal window, change your working directory to [meeting-minutes-generator](.), run the following commands. This will create and activate a virtual environment and install all the dependencies into it.
```sh
    chmod +x setup.sh
    ./setup.sh
```

# Execution
To start the application run the following command in [meeting-minutes-generator](.) folder.
```sh
    python3 main.py
```
