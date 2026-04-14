
# Discord DM Cleaner

A simple Discord self-bot that deletes your own messages from all DM channels.<br>
**Best for bulk deleting messages after being hacked and hacker mass dming everyone**<br>

## ⚠️ Disclaimer

> **Using self-bots violates Discord's Terms of Service.**<br>
> This tool is for **educational purposes only**.<br>
> Use at your own risk — **your account may be suspended or banned.** | **Security measures has been taken use with both email and number verified**

## Usage
> Add your discord token in `token` (required)<br>
> Set prefix (optional)<br>
> Set limit (default is 1) / Set limit to `None` for all messages<br>
> Send `cleandm` with your prefix added at first (no space) in any channel<br>

## Note
> Only deletes your own messages — it cannot delete messages sent by others<br>
> Automatically handles rate limiting (429 errors) and stops gracefully<br>
> Logs deleted message counts per DM to the console<br>
> limit controls how many messages are fetched per DM channel (None = unlimited)<br>

## Security
> No i dont log tokens<br>
> Use in private places (visual studio code / github codespace)
