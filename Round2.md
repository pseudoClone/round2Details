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

This is due to the fact that the script run and expects and input at runtime. For our case, we can avoid this by using environment variables to get the input from command line itself. However, since the container does start, we will ignore this since, the application logic is out of the scope.

6. For question 6, the [docker-compose.yml](./docker-compose.yml) has a compose configuration for a three tier application with a backend and a frontend and a Postgres database using the Postgres image; Alpine based. With this the size is reduced and the application is good to go.

7. For question 7, I have made a simple C++ application which logs this out: "Hello, this is a test for CI workflow". The CI will build the application and check if the output is correct. Here grep is used to check the redirected output of the program in a file. Details at: [CI FILE](./.github/workflows/ci.yml)

8. For this question, we will make a bash script that automatically run the build and test commands. We first make use of the shebang to tell that we will used bash as opposed to sh because bash has bashisms which might always come in handy and then we will clone a repo from Github to build it and test if the output is correct

9. We will create a .env file to keep our secrets and we will use python-dotenv to access it securely and validate some responses. For more details: [FILE](./.env). For the convinience and security, I will not upload the .env file to the remote repository.

10. For, question 10, we use run of the mill example of how Nginx can be setup for a reverse proxy. This load balancer will help reduce load of our application. Similar to how kubeapi-endpoint does. For further details: [NGINX Config](./nginx.conf). Assume that the application is in port 8080 and the server is listening at port 80.

12. For question, we use journalctl to evaluate why `sudo systemctl start docker.socket` runs quickly and `sudo systemctl start docker.service` run slowly. This is a synchronous behaviour that hampers me as a developer that is trying to run my microservices. As it turns out from the logs, the network connection failure in containerd is causing the downtime and hence, we should always stop containers from autostarting when loging in the system

13. For question 13, we use our previous Docker image with simple name calling application and try to analyze it logs. We use `docker logs -f vigilant_turing`. It quits immediately after failing to acquire the stdin from the user.

14. The web page has been deployed. Due to time constraints, a fully fledged application push could not be done. Here is the link for the [webpage](https://moonlit-babka-b6f07c.netlify.app/)