# Instagram Automation Bot

## Introduction

Hey there! I'm Samarth Jain, and I've been working on something pretty cool that I think you'll find useful. It's called the Instagram Automation Bot. Imagine being able to automate all the little tasks you do on Instagram, like liking posts, checking out user details, or even following and unfollowing people. This bot is all about making your Instagram life a bit easier and more efficient.

This bot is meant for educational purposes and personal use. It's not a magic wand that can solve all your Instagram problems, but it's a great way to learn and experiment with what's possible. Just remember, Instagram has its rules, and we don't want to break any of them. So, use this bot responsibly and keep an eye on Instagram's guidelines.

And one last thing: this project is a little side project I've been working on. It's not licensed or anything, but I'm sharing it here because I believe it could be a fun and educational tool for you. So, go ahead, explore what you can do with it, and maybe even learn a thing or two along the way.

Ready to dive in and see what you can do with the Instagram Automation Bot? Let's get started!

## Getting Started

To begin using this bot, follow these steps:

1. **Clone the Repository**: First, clone the repository to your local machine.

2. **Create a Command File**: Next, create a Python file where you'll write commands to call the functions provided by the bot.

## Using the Bot

Here's how to use the bot in your command file:

### 1. **Import the Bot Module**

Start by importing the bot module.

```javascript
python from InstaBot.Bot import *
```

### 2. **Log In to Instagram**

To log in to your Instagram account, use the `login` function by passing your username and password as arguments.

```javascript
python login("your_username", "your_password")
```

### 3. **Fetch User Details**

To retrieve user details such as post count, follower count, and description, use the `user_detail` function. You can pass a single username as a string or a list of usernames to fetch data for multiple users. The function returns the data in the form of a dictionary.

```javascript
user_detail("single_username")
```
```javascript
user_detail(["username1", "username2"])
```


### 4. **Convert The User Fetched Data To Excel**

To convert the user data to Excel data, use the `convert_excel` function. Pass the data you want to convert.

```javascript
convert_excel(data)
```


### 5. **Like Posts**

To like posts from a specific user, use the `like_n_post` function. Pass the username of the user whose posts you want to like, and optionally, the number of posts to like.

```javascript
like_n_post("username", 5) // Likes 5 posts from the user
```


### 6. **Follow a User**

To follow a user, use the `follow_user` function by passing the username of the user you want to follow.

```javascript
follow_user("username_to_follow")
```

### 7. **Unfollow a User**

To unfollow a user, use the `unfollow_user` function by passing the username of the user you want to unfollow.

```javascript
unfollow_user("username_to_unfollow")
```


### 8. **Check if an Account is Public**

To check if an account is public, use the `is_public_account` function. Pass the username of the account you want to check.



```javascript
 is_public_account("username")
```

### 9. **Check if a User Follows Another**

To check if one user follows another, use the `is_he_a_follower` function. Pass the username of the user you want to check and the username of the user you want to check against.



```javascript
is_he_a_follower("username_to_check", "username_to_check_against")
```

### 10. **Send a Message**

To send a message to a user, use the `send_message` function. Pass the username of the user you want to send a message to, the message text, and optionally, the number of times to send the message.

```javascript
send_message("username", "Hello!", 2) // Sends the message "Hello!" twice
```

### 11. **Upload a Post**

To upload a post, use the `upload_post` function. Pass the URL of the image you want to upload and the caption for the post.

```javascript
upload_post("https://example.com/image.jpg", "This is my caption")
```


## Conclusion

With these steps, you're all set to start using the Instagram Automation Bot. Enjoy automating your Instagram tasks!

## License

This project is licensed under the MIT License - see the [README.md](README.md) file for details.

