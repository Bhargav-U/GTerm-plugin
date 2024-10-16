# GTerm Plugin

Make your terminal smart by adding Gemini support!

Ensure the bot.py file is located in your home directory (~). If it's not, modify the following command by replacing location_of_file with the correct path to bot.py:
```bash
bot() {
    response=$(python3 location_of_file/bot.py "$1")
    echo "$response"
}
```

Open your terminal and enter the following command:

For bash:
```bash
gedit ~/.bashrc
```
For zsh:
```bash
gedit ~/.zshrc
```
Copy the contents from the bashrc_zshrc.txt file and paste them at the end of your .bashrc or .zshrc file.

Save and close the file.

In the terminal, run:
For bash:
```bash
source ~/.bashrc
```
For zsh:
```bash
source ~/.zshrc
```
Now you can use the bot command by typing:
```bash
bot "your question here"
```



