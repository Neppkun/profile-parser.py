# profile-parser.py

Parse Warframe profile data into useable Python objects. Forked from https://github.com/WFCD/profile-parser/

[![Discord](https://img.shields.io/discord/256087517353213954.svg?logo=discord)](https://discord.gg/jGZxH9f)

# VIBE CODE WARNING
This codebase was **ENTIRELY** rewritten into Python by [Anthropic](https://www.anthropic.com/)'s [Claude Opus 4.6](https://www.anthropic.com/claude/opus). It might not be the best code, but it works (probably), and that's all I needed it to do when I told it to make this.

## Installation

```shell
$ pip install git+https://github.com/Neppkun/profile-parser.py
```

## Example usage

```python
import requests

from profile_parser import ProfileParser

profile_data = requests.get(
    "https://content.warframe.com/dynamic/getProfileViewingData.php?n=${username}"
).json()
user = ProfileParser(profile_data)

print(user.profile.display_name)
```

If this data is stale, you can check the `Cache-Control` header of the response from DE's server to see how long to wait for retry, and you could have the above retry after that amount of time. However, this may cause _significant_ delay if the data is not saved/hydrated in a fully asynchronous or event-based timeframe.
