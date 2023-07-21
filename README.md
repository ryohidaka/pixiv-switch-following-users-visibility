# pixiv-switch-following-users-visibility

Switch visibility (public or private) of following users on Pixiv.

## Overview

This is a Python project that uses [pixivpy](https://github.com/upbit/pixivpy) to switch visibility users you are following.

## Notes

pixivpy is an unofficial API client. Please use it at your own risk. We do not take any responsibility for any damages caused by the use of this tool. Please use it with the understanding of the above.

## Installation

### Install the dependency packages

```zsh
$ pip install -r requirements.txt
```

### Set environment variables

```zsh
$ cp .env.example .env
```

| Name            | Description                  | Example   |
| --------------- | ---------------------------- | --------- |
| `USER_ID`       | Your Pixiv ID for logging in | `0123456` |
| `REFRESH_TOKEN` | Refresh token for Pixiv      | `***_***` |

### Run

#### Copy Mode (default)
`Source` remains the same, and follow `Target` users (**Copy**).

```zsh
# public => private (default)
$ python pixiv-following-user-to-csv/main.py --source public --target private --mode copy

# private => public
$ python pixiv-following-user-to-csv/main.py --source private --target public --mode copy
```

#### Move Mode
`Source` will be unfollowed and then followed on `Target`. (**Move**)

```zsh
# public => private (default)
$ python pixiv-following-user-to-csv/main.py --source public --target private --mode move

# private => public
$ python pixiv-following-user-to-csv/main.py --source private --target public --mode move
```

## Related

- [pixivpy](https://github.com/upbit/pixivpy)
