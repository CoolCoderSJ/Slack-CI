# Slack CI
Update a Slack canvas automatically via GitHub Actions!

If you're coming from Hack Club, Slack CI is already installed in the workspace. Just invite `@Slack CI` to a channel, run `/canvas`, and copy the canvas ID into one of the "remote" workflow files.

## Usage
This repository provides 4 workflows:
- Manual: Run the action manually, providing your canvas ID and file path at run time.
- Automatic: Specify a canvas ID and file path in the `.github/workflows/updateCanvasPush.yml` file, and the action will run automatically on push.
- Manual Remote: Same as manual, but sends data to the hosted version of Slack CI (so you don't need to make and install your own slack app)
- Automatic Remote: Same as automatic, but sends data to the hosted version of Slack CI (so you don't need to make and install your own slack app)

The workflows require a canvas ID and file path. Your contents are pulled directly from the repository, so you need to specify a file path relative to your repo. 

### Hosting
If you're not using the hosted version of Slack CI, you'll need to create a Slack app and install it to your workspace. Specify the bot token (not the app token) in a secret `SLACK_TOKEN` in an environment called `production`.

You can also choose to host the bot yourself. To do so, create a `.env` with `TOKEN=SLACK_BOT_TOKEN` and run `python bot.py`. Then, update the remote workflows to use your host instead.

If you choose to host a bot yourself, make sure to add /canvas to your bot's slash commands!

### Getting a Canvas ID
To get a canvas ID on slack, you can run `/canvas` in a channel with the bot. The bot will respond with a message containing the canvas ID.