# Instagram Automation Bot

## Introduction

Hello! I'm Samarth Jain, and I've developed an Instagram Automation Bot. This bot allows you to perform a wide range of tasks, from liking posts to fetching user details, among other functionalities.

## Getting Started

To begin using this bot, follow these steps:

1. **Clone the Repository**: First, clone the repository to your local machine.

2. **Create a Command File**: Next, create a Python file where you'll write commands to call the functions provided by the bot.

## Using the Bot

Here's how to use the bot in your command file:

1. **Import the Bot Module**: Start by importing the bot module.
```javascript
from InstaBot.Bot import *
```

2. **Log In to Instagram**: To log in to your Instagram account, use the `login` function by passing your username and password as arguments.
```javascript
login("your_username", "your_password")
```

3. **Fetch User Details**: To retrieve user details such as post count, follower count, and description, use the `fetch_user_detail` function. You can pass a single username as a string or a list of usernames to fetch data for multiple users. The function returns the data in the form of a dictionary.


## Conclusion

With these steps, you're all set to start using the Instagram Automation Bot. Enjoy automating your Instagram tasks!

## License

This project is licensed under the MIT License - see the [README.md](README.md) file for details.
