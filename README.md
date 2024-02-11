# OSRS Portal monitor and notifier

## Setup

> This guide assumes you are Ubuntu

Install git, python and python requests

```sh
sudo apt-get update && sudo apt-get install git python3 python3-requests
```

Clone the code

```sh
git clone https://github.com/OYsVbb09/StarMonitor 
```

and cd into the folder

```sh
cd StarMonitor
```

Then copy the `sample/env` to `.env`

```sh
cp samples/sample.env .env
```

And edit the `.env` file with your discord webhook endpoint and the 'target mention' role id

```sh
nano .env
```

## Running the code

```sh
VERBOSE=1 ./runner.sh
```

> or in 'Silent' mode:
>
> ```sh
> ./runner.sh
> ```
