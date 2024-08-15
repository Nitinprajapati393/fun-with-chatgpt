# CI Pipeline with Flask and ngrok

This repository demonstrates how to set up a CI pipeline using GitHub Actions for a Flask application, integrating ngrok to expose the application to the internet.

## Table of Contents

- [Project Overview](#project-overview)
- [Local Setup](#local-setup)
- [CI Pipeline Testing](#ci-pipeline-testing)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Setting Up GitHub Secrets](#setting-up-github-secrets)
- [License](#license)

## Project Overview

This project includes a Flask application that is tested and deployed using GitHub Actions. The CI pipeline uses ngrok to expose the application to the internet, allowing for external access and testing during the CI process.

## Local Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Install Dependencies**
    
    Ensure you have Python 3.11 installed. Then, install the required Python packages:

   ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt

3. **Install ngrok**

    Download and install ngrok:

   ```bash
    wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
    unzip ngrok-stable-linux-amd64.zip

4. **Set Up ngrok**
    
    Obtain an ngrok authentication token from the [ngrok dashboard](#https://dashboard.ngrok.com/).

    Run the following command to set up ngrok:

   ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt

5. **Start Flask Application and ngrok**

    Run your Flask application:

   ```bash
    nohup python run.py &

    Start ngrok to expose the Flask application:

    ```bash
    ./ngrok http 5000

## CI Pipeline Testing

1. **GitHub Actions Workflow**

The workflow automatically builds, tests, and deploys the application on push and pull request events.

2. **Check Workflow Status**

Go to the Actions tab in your GitHub repository to view the status of your workflows and logs.

3. **Debugging**

If the pipeline fails, check the logs for detailed error messages and adjust the workflow configuration as needed.

## GitHub Actions Workflow

The GitHub Actions workflow file .github/workflows/ci-pipeline.yml automates the following steps:

1. **Checkout Code**: Retrieves the code from the repository.
2. **Set Up Python**: Configures the Python environment.
3. **Install Dependencies**: Installs required Python packages.
4. **Update and Install ngrok**: Updates ngrok and installs the latest version.
5. **Install ngrok Authtoken**: Configures ngrok with your authentication token.
6. **Start Flask Application**: Runs the Flask application.
7. **Start ngrok**: Exposes the Flask application to the internet.
8. **Fetch ngrok Tunnel Information**: Retrieves the public URL from ngrok.
9. **Verify Flask Application**: Ensures the application is accessible via the ngrok URL.
10. **Run Tests**: Executes tests using pytest.
11. **Stop Flask Application and ngrok**: Cleans up processes.


## Setting Up GitHub Secrets

1. **Add ngrok Authentication Token**

    -   Go to your GitHub repository's **Settings.**
    -   Click on Secrets and variables > **Actions.**
    -   Click **New repository secret.**
    -   Name the secret **NGROK_AUTH_TOKEN** and paste your ngrok authentication token.






## Tech Stack

**Client:** N/A

**Server:** Flask, ngrok


## Support

For support, email workwidnitin@gmail.com 


## License

[MIT](https://choosealicense.com/licenses/mit/)

