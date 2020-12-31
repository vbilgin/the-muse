# The Muse

The Muse is a simple Slack bot that sends a random poem to a Slack channel every day at 9am PST.

## Tech
1. [PoetryDB](https://github.com/thundercomb/poetrydb) - This bot wouldn't be nearly as easy to implement if it wasn't for this API. It's super simple and easy to use.
2. [Heroku](https://heroku.com) - I'm running this bot in the free tier on Heroku. Heroku offers a free add-on for scheduling so that's what I'm using to schedule the run. I *could* do that with Python itself but I like being able to adjust it in a GUI whenever I want.