# OSRS Portal monitor and notifier

> [!IMPORTANT]  
> This repository has been archived!
> Refer to [irondvst/StarMonitor](https://github.com/irondvst/StarMonitor) instead

## Setup

> This guide assumes you are running on Ubuntu

Install git, python and python requests

```sh
sudo apt-get update && sudo apt-get install git python3 python3-requests
```

Clone the code (NOTE: original USERNAME "OYsVbb09" - use this to find mother code if needed)

```sh
git clone https://github.com/irondvst/StarMonitor 
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
