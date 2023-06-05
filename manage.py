#!/usr/bin/env python

import os
import sys
import logging
import json

from sacral.ai.configure import JiraGitHub

logging.basicConfig(level=logging.INFO)

def configure_jira_github(username, password, url, repo_name):
    """
    Configure Jira GitHub by logging into the Sacral.ai website and
    following the required steps.
    """
    jira_github = JiraGitHub()
    jira_github.configure(username, password, url, repo_name)

    # Validate the Jira Software credentials and return a response
    # indicating whether authentication was successful or not
    response = jira_github.validate()

    if response['status'] == 'success':
        logging.info('GitHub credentials successfully validated.')
    else:
        logging.error('Error validating GitHub credentials.')
        logging.error(response['message'])

def edit_configuration(title, username, url):
    """
    Edit the existing configuration with the given title, username, and URL.
    """
    jira_github = JiraGitHub()
    jira_github.edit_configuration(title, username, url)

def delete_configuration(title):
    """
    Delete the existing configuration with the given title.
    """
    jira_github = JiraGitHub()
    jira_github.delete_configuration(title)

def add_configuration(username, password, url, repo_name):
    """
    Add a new configuration with the given username, password, URL, and repository name.
    """
    jira_github = JiraGitHub()
    jira_github.add_configuration(username, password, url, repo_name)

def get_configurations():
    """
    Get the list of existing configurations.
    """
    jira_github = JiraGitHub()
    configurations = jira_github.get_configurations()
    logging.info('Configurations: %s', configurations)

def main():
    # Parse command line arguments
    if len(sys.argv) < 3:
        logging.error('Missing arguments.')
        sys.exit(1)

    command = sys.argv[1]
    params = json.loads(sys.argv[2])

    # Execute requested command
    if command == 'configure_jira_github':
        configure_jira_github(**params)
    elif command == 'edit_configuration':
        edit_configuration(**params)
    elif command == 'delete_configuration':
        delete_configuration(**params)
    elif command == 'add_configuration':
        add_configuration(**params)
    elif command == 'get_configurations':
        get_configurations(**params)
    else:
        logging.error('Unsupported command: %s', command)

if __name__ == '__main__':
    main()