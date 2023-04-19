# Github Pull Request Summary Report Script

This is a Python script that retrieves all open, closed, and in-progress pull requests from a specified Github repository and generates a summary report for the last 7 days. The summary report is output as an email-looking summary to the console.

## Prerequisites

- Python 3.8 or higher
- `requests` module (`pip install requests`)
- Github API access token

## Getting Started

1. Clone the repository or download the script `github_pr_summary.py`.
2. Install the `requests` module using the following command:
    ```
    pip install requests
    ```
3. Generate a Github API access token by following the steps described in [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
4. Set the `GITHUB_ACCESS_TOKEN` environment variable with your Github API access token.
    ```
    export GITHUB_ACCESS_TOKEN=<your_access_token>
    ```
5. Open the script `github_pr_summary.py` and modify the following variables:
    - `owner` - the owner of the Github repository
    - `repo` - the name of the Github repository
    - `manager` - a dictionary containing the name and email of the report recipient
    - `sender` - a dictionary containing the name, email, and role of the report sender
6. Run the script using the following command:
    ```
    python github_pr_summary.py
    ```

## Sample Output
    From: xxxx@welcome.com
    To: johndoe@company.xyz
    Subject: Summary of OPEN, CLOSED and IN PROGRESS Pull Requests from 2023-04-10 to 2023-04-17

    Hello John Doe,

    Here is a summary of pull requests for the brew repository from 2023-04-10 to 2023-04-17:

    Open Pull Requests:
    -------------------
    No OPEN pull requests in the last week

    Closed Pull Requests:
    ---------------------
    No CLOSED pull requests in the last week

    In-Progress Pull Requests (last week):
    ---------------------------------------
    No IN PROGRESS pull requests in the last week

    Thanks
    xxx xxx
    DevOps Engineer


## Running the script regularly

To generate reports regularly, you can use a task scheduler like `cron` on Linux or the Task Scheduler on Windows to run the script at specific times. For example, to generate a report every Monday at 9:00 AM, you can add the following entry to your `crontab` file:

    0 9 * * 1 /path/to/python /path/to/github_pr_summary.py >> /path/to/github_pr_summary.log

This will run the script every Monday at 9:00 AM and append the output to the `github_pr_summary.log` file. You can modify the frequency and output file name as per your requirements.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

