## CPU Usage Monitor

'' add image''

### Installation

First, Clone the project
`git clone https://github.com/brysonwaisi/power-consumption.git`
The requirements for running this project are `node`, `npm`, `django`

- To install dependencies, please `npm install` in the project client folder to pull all the required client dependencies.
- Use `pip install -r requirements.txt` to install the packages according to the configuration file requirements.txt for the server side.

### Firing up application

To fire up the application once all the project dependencies have been successfully installed you can build and consume the project simply by running `npm start` on the client and `python manage.py runserver` in your terminal console.

This will run the CRA build script under the hood to compile the UI layer. Moreover, it will spawn a Django instance serving as a forwarding server for the backend layer.
