# Expert Advice Chatbot for YouTube Creators

This project aims to provide a chatbot that offers expert advice to content creators looking to excel in the YouTube domain. With this chatbot, users can gain insights on creating compelling titles, brainstorming video ideas, receiving channel improvement suggestions, and much more. This chatbot is built using FastAPI and can be interacted with via a Discord bot.

## Development Environment Setup
We utilize a `.devcontainer` configuration to ensure a consistent development environment. This setup requires [VS Code](https://code.visualstudio.com/) and the [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/digiphd/chatbot_monorepo
    cd chatbot_monorepo
    ```

2. **Open the Project in VS Code:**
    - Launch VS Code.
    - Navigate to the cloned repository folder.
    - VS Code may automatically detect the `.devcontainer` configuration and prompt you to reopen the folder in a container. If so, accept the prompt.
    - If not, open the command palette (Ctrl+Shift+P or Cmd+Shift+P on Mac), and run the `Remote-Containers: Reopen Folder in Container` command.

3. **Install Dependencies:**
    - Once the container is up and running, the dependencies specified in the `api/requirements/requirements.txt` file will be automatically installed.

4. **Set Up Environment Variables:**
    - Copy the `.env.example` file to a new file named `.env`.
    - Fill in the necessary environment variables in the `.env` file.
    ```bash
    cp .env.example .env
    ```

5. **Run the FastAPI Application:**
    ```bash
    uvicorn api.main:app --host 0.0.0.0 --port 8000
    ```

## Setting Up Discord Application

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and click on "New Application".
2. Name your application and click "Create".
3. Under the Bot settings, click "Add Bot".
4. Take note of your bot token, as you will need it for the environment variables.
5. Invite the bot to your server using the link provided in the OAuth2 section.

## Deploying to Render

1. Fork this repository to your GitHub account.
2. Create a new Web Service on [Render](https://render.com/).
3. Select your repository and branch.
4. Set the build command to: `pip install -r api/requirements/requirements.txt && uvicorn api.main:app --host 0.0.0.0 --port 80`
5. Set the start command to: `bash start-dev.sh`
6. Add the necessary environment variables under the "Environment" section in Render dashboard.
7. Click "Save Web Service" to deploy your application.

## Usage

To interact with the chatbot on Discord, use the command `!ask` followed by your question. For example:

```bash
!ask How can I improve my video titles?
```

### Things to do:
- [x] Setup local dev environment
- [x] Get test servers running locally (frontend, bots, fastapi)
- [x] Get simple discord bot working with api locally
- [x] Add MIT License
- [] Deploy api to render - test
- [] Deploy discord bot to render - test
- [] Make sure long term memory persists at a user level (perhaps use mongodb)
- [] Add a simple next.js frontend for local testing
- [] Fine tune model based on youtube advice videos
- [] Write unit tests 