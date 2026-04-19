# Question Answer Description
1. Initialized Git Repository and pushed to Github and used [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
2. Created 2 branches. [Main](https://github.com/pseudoClone/round2Details/tree/main) is for main image builds and [develop](https://github.com/pseudoClone/round2Details/tree/develop) is for active development for teams. [Feature](https://github.com/pseudoClone/round2Details/tree/feature) is for keeping approved features from the team. For this scenario, it was done by a simple `git cherry-pick <hash>` from the develop branch. `git cherry-pick cb6726` was done and `cb6726` hash was found from `git log --oneline`
3. Simulated merge conflict by inserting changes to same code in two branches: [main](https://github.com/pseudoClone/round2Details/commit/924ed1bbf1f91e5197020ae822508653315f74ba) and [feat](https://github.com/pseudoClone/round2Details/commit/909c88dfc3fbeeb852f48f28bb42bd62389659a4). These were merged as follows: [LINK](https://github.com/pseudoClone/round2Details/commit/28228066715c955d57a46984764993fd40575955)

4. For question 4, the same repo contains the Dockerfile that is focused on optimization and small size. On changing the base image from Debain to Alpine, the image size was reduced in half. It was done using the following commands. ` docker buildx build -t simple-app .` and `docker buildx build -t simple-app-debian .` . And the size was reduced as follows: 
```
IMAGE                      ID             DISK USAGE   CONTENT SIZE   EXTRA
```
```
simple-app-debian:latest   19cf71389ceb        212MB         52.4MB
```
```
simple-app:latest          a4e9e34e04d2       96.6MB         23.8MB
```

5. On running the container in the repository as `docker run -d simple-app` (which is in detached mode), docker gives a hash for the container and a default tag for it. For my case, it was `2b758ddb0671` and `brave_neumann` respectively. On checking the logs of the container, using `docker logs -f brave_neumann`. I got the following logs:
```config
Traceback (most recent call last):
  File "/app/app.py", line 6, in <module>
    print(main())
          ~~~~^^
  File "/app/app.py", line 3, in main
    name = input("Enter your name: ")
EOFError: EOF when reading a line
```

This is due to the fact that the script run and expects and input at runtime. For our case, we can avoid this by using environment variables to get the input from command line itself.