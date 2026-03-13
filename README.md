# Free APIs for AI Agents 🤖⚙️

Welcome to **Free APIs for AI Agents**—a structured repository designed specifically to empower AI Agents, LLMs, and automation bots with real-time web capabilities.

## 🎯 The Goal

AI Agents often need to fetch live data (weather, crypto prices, economics, jokes, etc.) but get blocked by authentication walls or outdated training data. 

This repository solves that by providing a **massive, agent-friendly directory of 100% Free, No-Auth, HTTPS public APIs**. 

## 🚀 Get Started (Prompt for AI Agents)

If you are a human setting up your AI agent, **copy and paste the following prompt** to your agent to get it properly oriented with this repository:

> "Hey! We are working in a repository that contains a massive directory of free, public, no-auth APIs. To understand how to find and use these APIs to fetch live data, please read the `https://github.com/xyd945/free-api-for-agents/blob/main/free_public_apis/SKILL.md` file first. It acts as your primary instruction manual and contains a table of contents to all the available API categories."

## 🧠 Instructions for AI Agents

If you are an AI reading this repository, here is how you use it:

1. **Your Primary Skill File**: Navigate to `free_public_apis/SKILL.md`. This is your main instructional prompt.
2. **Browse the Categories**: The `SKILL.md` contains a Table of Contents pointing to specific markdown files in the `references/` directory (e.g., `finance.md`, `weather.md`).
3. **Find the Tool**: Read the relevant reference file to find the API documentation URL you need.
4. **Execute**: Either use your web browser tool to read the API docs, or guess the endpoint, and use `curl` or Python's `urllib` to fetch the data for the user! Some of the APIs has GET examples, more to add as we continue to improve the repo.

## 🛠️ Included Examples

To demonstrate what an agent can build using only the APIs found in this directory (with zero external dependencies), this repo includes two example Python scripts:

* `random_fact_combiner.py`: A fun, concurrent script that builds a dashboard out of 5 different entertainment APIs.
* `market_dashboard.py`: A serious executive summary script pulling live U.S. National Debt, Crypto, and Forex data.

Feel free to run them or inspect their source code to see how easily these APIs can be integrated.

## 🤝 Contributing
If you (human or agent) know of another reliable, free, and No-Auth API, please open a PR and add it to the relevant category in the `free_public_apis/references/` folder!

## Credits
This skill is built based on the [Public APIs](https://github.com/public-apis/public-apis) repository, kudos for everyone that contributed to that! 

## 📄 License
[MIT](LICENSE)
