#!/usr/bin/env python3

import argparse
from github import Github

# Replace with your GitHub personal access token
GITHUB_TOKEN = 'gitapikey'

def search_github(query, sort='stars', order='desc'):
    g = Github(GITHUB_TOKEN)
    repositories = g.search_repositories(query=query, sort=sort, order=order)
    return repositories

def main(query):
    repositories = search_github(query)

    for repo in repositories:
        print(f"{repo.full_name} ({repo.stargazers_count} stars) - {repo.html_url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search GitHub repositories for CVEs.")
    parser.add_argument("query", help="GitHub search query")

    args = parser.parse_args()

    main(args.query)
