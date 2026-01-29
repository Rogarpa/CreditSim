## Front stack
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

# Frontend

       
## Overview

REST API for getting simulations of loan amortization calculus.


## Universal Skills Involved
- Declarative design
- API Architecture


## Features


## Technologies Used 🤖

- **Frontend**:
    - **React**:
        - **Declarative** agains imperative approach, using custom hooks and modularizing components and request services.
        - **Conditional** rendering
        - **Hooks** usage as: useEffect and useState 
        - **Schema validator** api responses validation
        - **Local Storage** web browser persistance state
    - **Javascript**: Event handling 
    - **HTML5**: Prioritizing semantic tags, and descriptive ids, classes and nesting.

## Installation ⚙️⚙️

To start the application, you need to have installed:

- [Docker](https://www.docker.com/)

- [Docker-compose](https://docs.docker.com/compose/)

To install all the dependencies requred locally, run at package.json height:
```bash
#Docker Prerequisites
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg

#Add Docker's GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

#Add the Docker repository to Apt sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

#Install dependencies
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


# Install docker compose
sudo apt-get update
sudo apt-get install docker-compose-plugin

```

## Startup 🚀

To start the app 
The application is developed using [Docker-compose](https://docs.docker.com/compose/), so you can start the application with the following command:

```bash
docker compose up credit_sim
```

## Usage
1. Access the application via your browser at 8080 port (by default in vite configuration)
  (http://localhost:3000/).
- Fill the form for getting amortization table

[front]: https://github.com/Rogarpa/DevTools/tree/front?tab=readme-ov-file

[back]: https://github.com/Rogarpa/DevTools/tree/back?tab=readme-ov-file
