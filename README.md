# DLAI

## How to install the repository

### Prerequisites

- **Operative system**: Linux Ubuntu 22.04 LTS (Jammy Jellyfish)
- **Python3**: 3.10.12, with **pip3**
- **git-all**: installed
- **pytest**: recommended

No administrator privileges needed.

### Install the repository

- Find the path of the python3 command (for example: "/usr/bin/python3")
- Download the repository in the current directory:
~~~bash
    git clone https://github.com/StefanoMagriniAlunno/DLAI
    cd DLAI
~~~
- Set the current branch and install:
~~~bash
    git checkout your_branch
    ./install.sh /path/of/python3.10.12
~~~

It took longer than expected. ☕

## Repository contents

The master repository contains a basic template for hypothetical projects. It has two source folders:
- **sources**: This folder contains the first script, main.py, and a common module.
- **builds** and **libs**: These folders contain the source C code for shared objects.

In **assets**, we find images for this README and other graphics scripts.
In **templates**, we find code templates used by scripts.

In **documents**, we find the project documentation.


### Tools and Tests

"Test" and "tools" are folders for organizing Python scripts. Tools are used to show or analyze data, while tests are used for simple programs or proofs.

### Source design
Source code is organized in modules in sources and Python can call shared objects in libs. Each shared object is made from a single C project in builds. In brief: module organization in sources and sparse organization in builds.
Run make to refresh the list of shared objects.

### Handle scripts
This repo uses four scripts to manage libraries and modules:
- **add_lib.sh**: add a library template in builds
- **add_mod.sh**: add a module template in sources
- **rem_lib.sh**: remove a library from builds
- **rem_mod.sh**: remove a module from sources
- **history.log**: shows all actions with scripts.

### tasks.py
This file is a template for new branches. It installs packages and downloads data from the web during installation.
When yoy modify tasks.sh please reinstall the repository using **reinstall.sh**

## pre-commit
This repository uses a pre-commit system to manage updates:
1. **end-of-file-fixer --autofix**
2. **mixed-line-ending**
3. **check-yaml**
4. **check-json**
5. **check-docstring-first**
6. **sort-simple-yaml**
7. **pretty-format-json**
8. **flake8**
9. **doc8**
10. **autoflake**
11. **isort**
12. **shellcheck --exclude=='^templates/|install\.sh$'**
13. **mypy**
14. **black**
    
To check your code without committing it, run:
~~~bash
    pre-commit run --all-files
~~~

### Simple manual for GitHub

~~~bash
git checkout repo_name  # --> change repository branch
git branch  # get the current branch
git status  # get the status of current branch

git add .  # add updates in a queue (add again to update the queue)
git commit -m "message..."  # start pre-commit over the added queue
# if you not pass the test, try again:
# > git add .
# > git commit -m "message..."

# il problem persists, manual fix is required.
# fix code and try again...
# > git add .
# > git commit -m "message..."

git pull  # github compare commit with current version of code and try to merge yuor updates
git push  # fix changes
~~~

## Features

We find features of repository in **common** folder.

### common.logger

logger module manages log levels and define an abstract class.

<img src="assets/log_policy.png" title="Schema policy di log" style="zoom:100%;" />

#### exceptions
In this repository it is important manage and report all own exceptions:
- if you raise an exception, report in local documentation:
~~~python
"""
Raise
---
    - FileNotFound : _description_ [(traceback)]
"""
~~~
- if you use a own function with potential exceptions, use try to manage the exception:
  - if you ignore the exception report a warning
  - if you lunch the exception report an error (report the exception with (traceback) indication)
  - if you break the program report an error (without raise)

### common.temp

temp module manages temporary files in **temp**
