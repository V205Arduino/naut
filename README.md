# Elysia with Bun runtime

## Getting Started
To get started with this template, simply paste this command into your terminal:
```bash
bun create elysia ./elysia-example
```

## Development
To start the development server run:
```bash
bun run dev
```

Open http://localhost:3000/ with your browser to see the result.
```json
{
    {
        "timestamp": 12345,
        "type" : "book",
        "title": "Command and Control",
        "author": "Someone",
        "stars": 5
    },

    {
        "timestamp":12344,
        "type": "github",


    },
}
```

AI gen json example:
```json
[
    {
        "timestamp": 1672531200,
        "type": "book",
        "title": "Command and Control",
        "author": "Eric Schlosser",
        "stars": 4.8,
        "review": "A fascinating exploration of the dangers of nuclear weapons."
    },
    {
        "timestamp": 1672527600,
        "type": "blog",
        "title": "Understanding Microservices Architecture",
        "author": "Jane Doe",
        "url": "https://example.com/blog/microservices",
        "tags": ["microservices", "architecture", "development"]
    },
    {
        "timestamp": 1672524000,
        "type": "github",
        "event": "star",
        "repo_name": "octokit/octokit.js",
        "repo_url": "https://github.com/octokit/octokit.js",
        "actor": "johndoe"
    },
    {
        "timestamp": 1672520400,
        "type": "github",
        "event": "commit",
        "repo_name": "octokit/octokit.js",
        "repo_url": "https://github.com/octokit/octokit.js",
        "commit_message": "Fix authentication bug",
        "commit_sha": "a1b2c3d4e5f6",
        "actor": "johndoe"
    },
    {
        "timestamp": 1672516800,
        "type": "github",
        "event": "pull_request",
        "repo_name": "octokit/octokit.js",
        "repo_url": "https://github.com/octokit/octokit.js",
        "pr_title": "Improve error handling",
        "pr_number": 123,
        "pr_url": "https://github.com/octokit/octokit.js/pull/123",
        "actor": "johndoe"
    },
    {
        "timestamp": 1672513200,
        "type": "github",
        "event": "issue",
        "repo_name": "octokit/octokit.js",
        "repo_url": "https://github.com/octokit/octokit.js",
        "issue_title": "Documentation update needed",
        "issue_number": 456,
        "issue_url": "https://github.com/octokit/octokit.js/issues/456",
        "actor": "johndoe"
    },
    {
        "timestamp": 1672509600,
        "type": "github",
        "event": "fork",
        "repo_name": "octokit/octokit.js",
        "repo_url": "https://github.com/octokit/octokit.js",
        "forkee_repo_name": "johndoe/octokit.js",
        "forkee_repo_url": "https://github.com/johndoe/octokit.js",
        "actor": "johndoe"
    },
    {
        "timestamp": 1672506000,
        "type": "blog",
        "title": "The Future of Web Development",
        "author": "John Doe",
        "url": "https://example.com/blog/future-of-web-dev",
        "tags": ["web development", "trends", "technology"]
    }
]
```