# React + Vite + Flask Starter Template

## Table of Contents

- [Overview](#overview)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Scripts](#scripts)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This project is a full-stack application that combines a **React** frontend built with **Vite** and a **Flask** backend. It demonstrates how to set up a modern development environment with hot module replacement (HMR), linting, and seamless integration between the frontend and backend.

## Screenshots

![Dark theme](https://i.ibb.co/wd8y9Zr/dark-theme-screenshot.png)

![Light theme](https://i.ibb.co/y5mMdvD/light-theme-screenshot.png)

## Project Structure

```bash
project-root/
├── client/
│   ├── public/
│   │   ├── flask.svg
│   │   └── vite.svg
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── assets/
│   │       └── react.svg
│   ├── README.md
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── eslint.config.js
│   ├── App.css
│   └── index.css
├── server/
│   └── app.py
├── .gitignore
├── LICENSE
├── Pipfile
├── Pipfile.lock
└── requirements.txt
```

## Features

- **React Frontend**: Built with React and Vite for a fast development experience.
- **Flask Backend**: Simple API endpoint to demonstrate backend integration.
- **Hot Module Replacement (HMR)**: Instant updates without full page reloads.
- **ESLint Integration**: Ensures code quality and consistency.
- **Proxy Setup**: Seamless communication between frontend and backend during development.
- **Deployment Ready**: Configured for production builds with Vite and Gunicorn.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- **Node.js** (v14 or later)
- **npm** (comes with Node.js) or **yarn**
- **Python** (v3.12)
- **Pipenv**

### Installation

1. **Clone the Repository**

   ```bash
   npx degit https://github.com/silvanos-eric/flask-react-starter.git <my-project>
   cd your-repo
   ```

    Replace `<my-project>` in the above comamnd with your desired project name
    e.g:

    ```bash
     npx degit https://github.com/silvanos-eric/flask-react-starter.git phase_5_project
     cd phase_5_project
    ```

2. **Set Up the Backend**

   Navigate to the project root and install Python dependencies using Pipenv:

   ```bash
   pipenv install
   ```

   Activate the Pipenv shell:

   ```bash
   pipenv shell
   ```

3. **Set Up the Frontend**

   Navigate to the `client` directory and install Node.js dependencies:

   ```bash
   cd client
   npm install
   ```

4. **Initializing git**

    - Create a an empty git repository on a github account of your choice.
    - The name of the repository should be guided by the name of the folder you selected in [step 1](#installation) above

        In my case, I named my copy of the starter project `phase_5_project`.

        So my new github repository will consequently be named `phase_5_project`

        ![Creating a new repo](https://i.ibb.co/kQ7VHVv/flask-react-starter-creating-a-new-repo.png)

    - ***Note***: Do not initalize the repository with a `README.md` file, a `.gitignore` file or a `LICENSE.md` file as demonstrated below

        ![Repo setup](https://i.ibb.co/TYKBBJ6/flask-react-starter-repo-setup.png)

    - Click on the create repository button

        ![Create repo](https://i.ibb.co/SmN9svN/create-repo.png)

    - Switch back to your copy of the starter project and initialize git

      ![Initializing git](https://i.ibb.co/mS5qSHk/flask-react-starter-initialize-git.png)

    - Create your first commit

      ![First commit](https://i.ibb.co/kJ7XQjv/initial-commit.png)

    - Go back to your newly created repository on github, and follow the instructions for pushing an existing repository from the command line

      ![Push existing repo](https://i.ibb.co/4g4JwPZ/push-an-existing-repo.png)

### Running the Application

1. **Start the Flask Backend**

   Ensure you're in the Pipenv shell and run from the `server` directory:

   ```bash
   python server/app.py
   ```

   The backend server will start on `http://localhost:5555`.

2. **Start the React Frontend**

   Open a new terminal, navigate to the `client` directory, and run:

   ```bash
   npm run dev
   ```

   The frontend application will start on `http://localhost:5173` and proxy API requests to the Flask backend.

3. **Access the Application**

   Open your browser and navigate to `http://localhost:5173` to see the application in action.

## Scripts

### Backend

- **Run Server**

  ```bash
  python server/app.py
  ```

### Frontend (Client)

- **Start Development Server**

  ```bash
  npm run dev
  ```

- **Build for Production**

  ```bash
  npm run build
  ```

- **Preview Production Build**

  ```bash
  npm run preview
  ```

- **Lint Code**

  ```bash
  npm run lint
  ```

## Technologies Used

- **Frontend**

  - [React](https://react.dev/)
  - [Vite](https://vite.dev/)
  - [ESLint](https://eslint.org/)
  - [SWC](https://swc.rs/) for Fast Refresh

- **Backend**

  - [Flask](https://flask.palletsprojects.com/)
  - [Gunicorn](https://gunicorn.org/)

- **Others**
  - [Pipenv](https://pipenv.pypa.io/)
  - [Python 3.12](https://www.python.org/)
  - [Node.js](https://nodejs.org/)

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact **Silvanos Eric** at [ericoderito@gmail.com](mailto:ericoderito@gmail.com).
