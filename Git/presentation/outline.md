# Outline

- TODOs
  - [ ] Sicherstellen dass es auch einen Mehrwert für nicht-Programmierer hat
  - [ ] Graphen für alles wichtige
  - [ ] try out without SSH key
  - [x] Make the icons: font awesome notice
  - [ ] Add pauses
  - [ ] Add Github GUI
  - [ ] Add information on how to add github GUI

- Git-GUIs
    - GH-GUI is not available on Linux
    - SourceTree is not available on Linux
    - Gitg doesnt work on mac
    - Tower doesnt work on Linux
    - Gitkraken is not free
    - vscode integration is... vscode specific
    - lazygit is great... but not more helpful to beginners than the CLI

## Motivation

- Goals

- Original Problem:
  - People wanted to collaborate
  - TODO bla bla what they did back then with USB sticks and alike

- Solution: Git!
  - A "distributed version control system"
  - Initially developed for the linux kernel
  - You can bundle your set of changes into names updates, called commits
  - This way, everyone can search and work with that history.
  - TODO: Mal lesen was andere so schreiben
  - Show the guitar hero history thingy on the right side

- Git is not GitHub! Git is not GitLab!
  - Maybe many have heard about github or to a lesser extend gitlab
  - Although they use
  - Think of Mail: Google Mail and Outlook

- Why to use git:
  - Traditonally: Collaborate with others
  - Manage multiple, actively worked on versions
    - Imagine you want to build your code and someone would type in there! It would break!
  - Version your code, take more risk, roll back mistakes!
  - Make your code more discoverable
    - Its common (and reasonable) to google `MY PROBLEM github`
    - Github becomes more of a social network, thus more discoverability
  - Use Github/Gitlab as an portfolio for future employers
  - (People expect it)

## Theory

- How does Git work?
    - Git projects are called **repositories** (i.e. repos)
        - Thats where the code goes in
    - There are 2 ways to create a Git repository:
        - **Initialize** a new folder (Create)
        - **Clone** an existing repo from a remote server (Download)
    - This means that it is **local** on your device, not synced like a Cloud!
    - This is a normal folder, you can work in there with your normal tools
    - Once you have finished something, you can bundle it into an update
        - This is called a **commit**.

- What does the distributed mean?
    - Once you **initialize** or **clone** the repo, it is local on your device.
        - it is **not** on the remote server!
    - Every developer has its local version that does not change automatically
    - Instead, one can manually
        - **Pull** the newest commits from the server or
        - **Push** the local commits to the server!

- How does a commit work (bad headline name)
    - Git is (mainly) for text files!
        - what is a text file
        - docx is not a text file
    - show how a diff looks
    - One can also put in non-text files
        - but this means that theyll always be fully replaced
            - this means that the advantage of those beautiful diffs get lost!
        - Thus, it mainly makes sense for non-changing, related assets such as
            - images
            - sound files
            - 3D models
    - When should one commit:
        - If you can describe what you have done.
            - Think of an experiment log.
                - You wouldn't write "I am currently filling the 41st ml into this flask!"
        - Think of what commits are for:
            - Better Understanding for others
            - Better Understanding for your own previous work (you will forget)


## Getting Started

- Setting Up Git
  - Install, and show links to instructions
  - Note that we do that together in the exercise

- Initial configuration:
    - Check if git installed
    - Username... Password...

- Create repository
    - Lets say you have some code you want to start to version...
    - Web UI

- Go into folder with some existing data
    - left side right side two terminals
    - git init
    - git status
        - Staged erklären
    - git add
    - git status
    - git rm (--cached)

- Commits
    - git commit -m "MESSAGE"
    - git log (--oneline)

- Push / Pull
    - split terminal sides again
    - push up
    - pull down

- Remote repos
    - clone
    - git log --oneline
    - edit file
    - git diff

## GitHub GUI

- One slide introducing GitHub GUI
  - Left side: CLI vs GUI
  - Right Side: GitHub GUI

- Show how cloning is done

- Show how committing and push/pull is done

- Maybe show how the status is shown?


## Advanced
- Merge Konflikte
  - remember that it is distributed, i.e. everybody works on their own device
  - person A and B clone the repo
  - person A updates `foo.py`, commits it and pushes it
  - next day, B does the same
  - then, B wants to push it, not knowing about A's previosu update
  - what now
  - Wann treten sie auf
  - Wie behebt man sie

- Branching
  - u.a. um sich nicht um merging sorgen machen zu müssen
  - und für organisatorische struktur
    - üblich nen feature branch zu haben (beispiel)
  - Bild hiervon: <https://marc.info/?l=linux-kernel&m=139033182525831>
  - Does github have a good guitar hero looking tool?

- Git blame

- Gitignore
  - Zeig githubs eigene sammlung
  - Wofür
    - Kram der nicht online sein soll
    - Temporärer Kram

- Git bisect

## Conclusion
- Summary
  - todo reiterate
  -  oh shit, git
