# music-recs
A Python application to get music recommendations.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation
Fork this [remote repository](https://github.com/stsikata/nusic-recs.git) and clone a remote copy on your local computer.

Navigate to the local copy from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd music-recs
```

Use Anaconda to create and activate a new virtual environment called "music-recs-env":

```sh
conda create -n music-recs-env python=3.8 # (first time only)
conda activate music-recs-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

## Setup

In your local repository's root directory, create a new file called ".env". Update the contents of the ".env" file to specify your desired username:

    SPOTIPY_CLIENT_ID="YOUR_APP_CLIENT_ID"
    SPOTIPY_CLIENT_SECRET="YOUR_APP_CLIENT_SECRET"

## Usage

Run the game script:

```py
python artist_recs.py
```