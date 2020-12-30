# Horoscope Cli project

A project done for the python course at Epita / MTI.
Project made with Typer Boilerplate project as base, realised by CHUNG Feng, FRANEL Thomas, GARDEBOIS Jeanne and GRACIAS Alister. 

# Typer Boilerplate

A boilerplate making use of [typer](https://github.com/tiangolo/typer) + [pytest](https://github.com/pytest-dev/pytest) + docker.
This repository has been made for my students and my future-self, maybe for some people passing by too, who knows.

# Requirements

Docker.

Windows users: sorry, you wont be able to use the tiny shell scripts, please check the note at the end.
They don't do much in the present repository, this is a personal habit to have `run.sh` and `runtests.sh` at the root of my repositories.

# Usage

## Build container first

```bash
./install.sh
```

## Running commands with help

```bash
./run.sh --help
```

Or, as arguments are passed around :

```bash
./run.sh gethoroscopefromapi --help
./run.sh gethoroscopefromscrapper --help
```

## Testing

```bash
./runtests.sh
```
Or, as arguments are passed around, you can pass your prefered pytest flags.

```bash
./runtests.sh --pdb
```

## Debugging

In case you want to enter your container environment :

```bash
docker build . -t horoscopecli
docker run -it --entrypoint bash horoscopecli
```