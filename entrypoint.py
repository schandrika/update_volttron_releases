#!/usr/bin/env -S python3 -B

# NOTE: If you are using an alpine docker image
# such as pyaction-lite, the -S option above won't
# work. The above line works fine on other linux distributions
# such as debian, etc, so the above line will work fine
# if you use pyaction:4.0.0 or higher as your base docker image.

import sys
import os

import toml
from github import Github
import os

def main():
    print(os.environ)
    client = Github(os.environ["GITHUB_TOKEN"])
    client.get_repo(os.environ["GITHUB_REPOSITORY"])

    with open('pyproject.toml', 'r') as f:
        toml_dict = toml.load(f)
    dependencies_ = toml_dict['tool']['poetry']['dependencies']
    for lib in dependencies_:
        if lib.startswith("fake"):
            # if it has a pre-release=true flag, remove that flag
            if isinstance(dependencies_[lib], dict) and dependencies_[lib].get('allow-prereleases'):
                # del lib_details['allow-prereleases']  # this create dependencies.volttron-something as a new config entry
                # so use just version. Could switch to tomllib with python 3.11
                dependencies_[lib] = dependencies_[lib]["version"]

    with open('new_toml_file.toml', 'w') as f:
        toml.dump(toml_dict, f)

if __name__ == "__main__" :
    main()
    # Rename these variables to something meaningful
    # input1 = sys.argv[1]
    # input2 = sys.argv[2]
    #
    #
    # # Fake example outputs
    # output1 = "Hello"
    # output2 = "World"
    #
    # # This is how you produce workflow outputs.
    # # Make sure corresponds to output variable names in action.yml
    # if "GITHUB_OUTPUT" in os.environ :
    #     with open(os.environ["GITHUB_OUTPUT"], "a") as f :
    #         print("{0}={1}".format("output-one", output1), file=f)
    #         print("{0}={1}".format("output-two", output2), file=f)
