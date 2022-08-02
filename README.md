# TU’22 Tracks rishabhraizada

# Git and Docker

- Git commands
    - git checkout `branch`: To switch branch
    - git checkout -b `branch`: Create a new branch from current branch
    - git branch -d `branch`: Delete branch
    - git log: View git commit history
    - git push --set-upstream origin `branch`: Push new branch to remote
    - git rebase -i HEAD~n: Interactive window for commits HEAD to the nth commit to squash, pick, reword, fixup, etc 

<br>

- Docker commands
    - docker build -t `image`: Build docker image
    - docker create `image`: Create docker container from image
    - docker create `image`: Create docker container from image
    - docker start `container_id`: Start docker container 
    - docker run `image`: Create & start docker container from image 
    - docker-compose up: Create & run all services in docker-compose.yml file
    - docker-compose down: Stop all running containers 

### Screenshots
- Assignment-1: Add GET api request with query parameters
![docker-1](https://user-images.githubusercontent.com/110235735/182478865-1a8c93d2-1e8e-4303-bd78-cd6b7208756f.png)

- Assignment-2.1: Initialise two containers with hot reloading
![docker-2 1](https://user-images.githubusercontent.com/110235735/182478925-7d26e149-eea4-4a51-818e-54d16a037375.png)

- Assignment-2.2: ADD POST api with request body and server-1 as proxy
![docker-2 2](https://user-images.githubusercontent.com/110235735/182478923-0d5085bb-f538-42bc-b816-c5ae20e7e010.png)

- Assignment-2.3: Merge docker-2 and Rebase & squash commits

![docker-2 6](https://user-images.githubusercontent.com/110235735/182478900-e18716bc-079c-444a-b11f-e39cc310571b.png)
![docker-2 3](https://user-images.githubusercontent.com/110235735/182478918-600c3723-3dec-4073-bba2-02841d7a93e2.png)

- Assignment-2.4: Automate devspaces using .gitpod.yml
![docker-2 4](https://user-images.githubusercontent.com/110235735/182478912-b9b778d1-b0e2-4c83-bda1-8c557df217a2.png)

- Assignment-2.5: Add Github Action to validate build
![docker-2 5](https://user-images.githubusercontent.com/110235735/182478908-772f7c49-91c8-4ca8-a810-d6f651d88ed5.png)

