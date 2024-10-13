import { Octokit } from "@octokit/core";
import dotenv from 'dotenv';

dotenv.config();

const githubAPIKey = process.env.GITHUB_ACCESS_TOKEN;

const octokit = new Octokit({
  auth: githubAPIKey
});

// Variable to store the latest data
let latestData: any = null;

// Default poll interval in seconds (in case header is missing)
const DEFAULT_POLL_INTERVAL = 60;

// Function to fetch user events and update latestData
async function updateUserEvents() {
  try {
    const response = await octokit.request('GET /users/{username}/events', {
      username: 'V205Arduino',
      headers: {
        'X-GitHub-Api-Version': '2022-11-28'
      }
    });

    // Update the latest data
    latestData = response.data;

    // Extract the poll interval from response headers
    const pollIntervalHeader = response.headers['x-poll-interval'];
    const pollIntervalSeconds = pollIntervalHeader
      ? parseInt(pollIntervalHeader, 10)
      : DEFAULT_POLL_INTERVAL;

    console.log(`Data updated. Next update in ${pollIntervalSeconds} seconds.`);
    
    // Process and log the useful data
    processAndLogData(latestData);
    console.log(latestData)

    // Schedule the next update
    setTimeout(updateUserEvents, pollIntervalSeconds * 1000);
  } catch (error) {
    console.error('Error fetching user events:', error);

    // Retry after a default interval if an error occurs
    setTimeout(updateUserEvents, DEFAULT_POLL_INTERVAL * 1000);
  }
}

// Function to process and log useful data
function processAndLogData(data: any[]) {
  data.forEach(event => {
    // Safely access the type, repo name, and created_at fields
    const type = event?.type ?? 'Unknown Type';
    const repoName = event?.repo?.name ?? 'Unknown Repo';
    const createdAt = event?.created_at ?? 'Unknown Date';

    console.log(`Event Type: ${type}, Repo: ${repoName}, Created At: ${createdAt}`);

    // Access the payload safely
    const payload = event?.payload ?? {};

    switch (type) {
      case 'PushEvent':
        const commits = payload?.commits ?? [];
        console.log(`Commits: ${commits.map((commit: any) => commit?.sha ?? 'Unknown SHA').join(', ')}`);
        break;
      case 'WatchEvent':
        // Correctly access the actor.login from the event object
        const watcher = event?.actor?.login ?? 'Unknown Actor';
        console.log(`Watched by: ${watcher}`);
        break;
      case 'StarEvent':
        // Correctly access the actor.login from the event object
        const starGiver = event?.actor?.login ?? 'Unknown Actor';
        console.log(`Starred by: ${starGiver}`);
        break;
      case 'PullRequestEvent':
        const prAction = payload?.action ?? 'Unknown Action';
        const prNumber = payload?.number ?? 'Unknown Number';
        console.log(`PR Action: ${prAction}, PR Number: ${prNumber}`);
        break;
      case 'IssuesEvent':
        const issueAction = payload?.action ?? 'Unknown Action';
        const issueNumber = payload?.issue?.number ?? 'Unknown Number';
        console.log(`Issue Action: ${issueAction}, Issue Number: ${issueNumber}`);
        break;
      default:
        console.log(`Other event type: ${type}`);
    }
  });
}

// Start the update loop
updateUserEvents();

// Function to get the latest data
export function getLatestData(): Promise<any> {
  return new Promise((resolve, reject) => {
    if (latestData !== null) {
      resolve(latestData);
    } else {
      const intervalId = setInterval(() => {
        if (latestData !== null) {
          //processAndLogData(latestData)
          
          clearInterval(intervalId);
          resolve(latestData);
        }
      }, 100);
    }
  });
}