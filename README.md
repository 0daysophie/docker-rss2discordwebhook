# Docker RSS feed fetcher for Discord webhooks

A script that fetches a RSS feed every 24 hours and sends the feed items to a Discord channel.
The current example config is built for the BleepingComputer RSS feed.
This uses the official Python Docker image.

## Installation (Dockerfile)
1. `git clone https://github.com/0daysophie/docker-rss2discordwebhook`
2. `cd docker-rss2discordwebhook`
3. Modify webhook.py accordingly
4. `docker build -t docker-rss2discordwebhook .`
5. `docker run -it --rm --name docker-rss2discordwebhook-1 docker-rss2discordwebhook`


## Installation (UGreen NAS Docker applet):
1. Get the official Python Docker image
2. Set the Webhook URL in the webhook.py script and modify the script accordingly
3. Set a volume to `<scriptfolder>:/app`
4. Upload `webhook.py`, `requirements.txt` and `start.sh` to the scriptfolder set in step 3
5. Set `bash` `/app/start.sh` as startup command
6. Enable Container auto-reboot/autostart
7. Run the container
