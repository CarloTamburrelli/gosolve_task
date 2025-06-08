## Find the index of a number

Make sure you have Docker and Docker Compose installed.

To build and run the project in foreground:

```bash
make up
```

In background:

```bash
make up-detached
```

The `make up` command will build the docker images and starts the two containers:


- **frontend**: React + Vite
- **backend**: Flask

The configuration file `.env` is located in the root of the project.


To run tests:

```bash
make test
```


