## CPU Usage Monitor

![cpu](https://github.com/brysonwaisi/power-consumption/blob/main/power_consumption/static/images/cpu.png)

### Installation

First, Clone the project
`git clone https://github.com/brysonwaisi/power-consumption.git`

The requirements for running this project are `python` and `django` installed

- Use `pip install -r requirements.txt` to install the packages according to the configuration file requirements.txt.

### Firing up application

To fire up the application once all the project dependencies have been successfully installed you can build and consume the project simply by running `python manage.py runserver` in your terminal console.

This will spawn a Django instance serving as a forwarding server for the backend layer, and serve the templates.

Access the UI functionality at `http://127.0.0.1:8000/monitor_cpu/`
