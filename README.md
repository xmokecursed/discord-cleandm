
# Discord DM Cleaner

A simple Discord self-bot that deletes your own messages from all DM channels.\n
**Best for bulk deleting messages after being hacked and hacker mass dming everyone**

## ⚠️ Disclaimer

> **Using self-bots violates Discord's Terms of Service.**\n
> This tool is for **educational purposes only**.\n
> Use at your own risk — **your account may be suspended or banned.** | **Security measures has been taken use with both email and number verified**

## Usage
> Add your discord token in `token` (required)\n
> Set prefix (optional)\n
> Set limit (default is 1) / Set limit to `None` for all messages\n
> Send `cleandm` with your prefix added at first (no space) in any channel\n

## Note
> Only deletes your own messages — it cannot delete messages sent by others\n
> Automatically handles rate limiting (429 errors) and stops gracefully\n
> Logs deleted message counts per DM to the console\n
> limit controls how many messages are fetched per DM channel (None = unlimited)

## Security
> No i dont log tokens\n
> Use in private places (visual studio code / github codespace)
