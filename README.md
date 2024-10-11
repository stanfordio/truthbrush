# truthbrush
Truthbrush is an API client for Truth Social. Truthbrush is built and maintained by the [Stanford Internet Observatory](https://io.stanford.edu).

Currently, this tool can:

* Search for users, statuses, groups, or hashtags
* Pull a user's statuses
* Pull the list of "People to Follow" or suggested users
* Pull "trending" hashtags
* Pull "trending" Truth posts
* Pull ads
* Pull a user's metadata
* Pull the list of users who liked a post
* Pull the list of comments on a post
* Pull "trending" groups
* Pull list of suggested groups
* Pull "trending" group hashtags
* Pull posts from group timeline

Truthbrush is designed for academic research, open source intelligence gathering, and data archival. It pulls all data from the publicly accessible API.

## Installation

Truthbrush is not yet available on PyPI. To install it, run `pip install git+https://github.com/stanfordio/truthbrush.git`, or clone the repository and run `pip3 install .`. Provided your `pip` is setup correctly, this will make `truthbrush` available both as a command and as a Python package. **Note that Truthbrush requires Python 3.9 or higher.**

After installation, you will need to set your Truth Social username and password as environmental variables.

`export TRUTHSOCIAL_USERNAME=foo`

`export TRUTHSOCIAL_PASSWORD=bar`

You may also set these variables in a `.env` file in the directory from which you are running Truthbrush.

## CLI Usage

```text
Usage: truthbrush [OPTIONS] COMMAND [ARGS]...

Options:
  --help     Show this message and exit.


Commands:
  search            Search for users, statuses or hashtags.
  statuses          Pull a user's statuses.
  suggestions       Pull the list of suggested users.
  tags              Pull trendy tags.
  trends            Pull trendy Truths.
  ads               Pull ads.
  user              Pull a user's metadata.
  likes             Pull the list of users who liked a post
  comments          Pull the list of oldest comments on a post
  groupposts        Pull posts from a groups's timeline
  grouptags         Pull trending group tags.
  grouptrends       Pull trending groups.
  groupsuggestions  Pull list of suggested groups.

``````

**Search for users, statuses, groups, or hashtags**

```bash
truthbrush search --searchtype [accounts|statuses|hashtags|groups] QUERY
```

**Pull all statuses (posts) from a user**

```bash
truthbrush statuses HANDLE
```

**Pull "People to Follow" (suggested) users**

```bash
truthbrush suggestions
```
**Pull trendy tags**

```bash
truthbrush tags
```
**Pull ads**

```bash
truthbrush ads
```

**Pull all of a user's metadata**

```bash
truthbrush user HANDLE
```

**Pull the list of users who liked a post**

```bash
truthbrush likes POST --includeall TOP_NUM
```

**Pull the list of oldest comments on a post**

```bash
truthbrush comments POST --includeall --onlyfirst TOP_NUM
```

**Pull trending group tags**

```bash
truthbrush grouptags
```

**Pull trending groups**

```bash
truthbrush grouptrends
```

**Pull list of suggested groups**

```bash
truthbrush groupsuggestions
```

**Pull posts from a group's timeline**

```bash
truthbrush groupposts GROUP_ID
```

## Contributing

Contributions are encouraged! For small bug fixes and minor improvements, feel free to just open a PR. For larger changes, please open an issue first so that other contributors can discuss your plan, avoid duplicated work, and ensure it aligns with the goals of the project. Be sure to also follow the [code of conduct](CODE_OF_CONDUCT.md). Thanks!

Development setup (ensure you have [Poetry](https://python-poetry.org/) installed):

```sh
poetry install
poetry shell
truthbrush --help # will use your local copy of truthbrush
```


If you prefer not to install Poetry in your root environment, you can also use Conda:

```sh
conda create -n truthbrush-env python=3.10
conda activate truthbrush-env

conda install -c conda-forge poetry
poetry install
```

To run the tests:

```sh
pytest

# optionally run tests with verbose logging outputs:
pytest --log-cli-level=DEBUG -s

# optionally run tests with suppressed warnings:
pytest --disable-pytest-warnings
```

Please format your code with `black`:

```sh
black .
```

### Continuous Integration

The Continuous Integration build on GitHub Actions is controlled via the "python-app" workflow file. To make the build pass, the environment variables `TRUTHSOCIAL_USERNAME` and `TRUTHSOCIAL_PASSWORD` must be set as GitHub repository secrets.


## Wishlist

Support for the following capabilities is planned:

- ...nothing right now! (Got an idea? Submit an issue/PR!)
