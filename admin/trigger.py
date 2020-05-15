import os
import subprocess
import sys
import time

for project in os.listdir("projects"):
    if ".timestamp" in os.listdir(os.path.join("projects", project)):
        filename = os.path.join("projects", project, ".timestamp")
        with open(filename, "w") as timestamp:
            print("Written timestamp for %s" % filename)
            timestamp.write(str(time.time()))

def cmd(*args):
    print("Calling:", args)
    res = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode != 0:
        print("Error occurred on calling: %s" % ' '.join(args))
        print(res.stderr.decode("utf-8"))
        sys.exit(res.returncode)
    return res

cmd("git", "checkout", "-b", "trigger-builds-%s" % time.time())
cmd("git", "config", "user.email", "andymckay@github.com")
cmd("git", "config", "user.name", "Andy McKay")
cmd("git", "commit", "-m", "Pushes on the project", "-a")
cmd("gh", "pr", "create", "-t", "Trigger automatic builds", "-b", "Automatic pull request trigger")
print("Successfully created PR.")