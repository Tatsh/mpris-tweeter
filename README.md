# Requirements

* Python 2.7
* [D-Bus](http://dbus.freedesktop.org/) (comes with virtually every distro)
* [tweepy](http://tweepy.github.com/)

## Gentoo

```bash
# echo 'dev-python/tweepy ~amd64'
emerge dev-python/tweepy
```

# Configuration
Before running the script, set up a file `~/.mpris-twitter-listener.yml` that looks like the following:

```yaml
consumer_key: random_string_from_twitter
consumer_secret: random_string_from_twitter

access_token: numbers-random_string_from_twitter
access_token_secret: random_string_from_twitter
```

Get these keys by [creating an application on Twitter's development page](https://dev.twitter.com/apps/new). Put anything for the required fields.

# Running the script

```bash
./bin/mpris-twitter-listener
```

Debug mode:

```bash
./bin/mpris-twitter-listener -v
```

# Appending text to tweet based on artist name

The artist information exposed from D-Bus is a list (in the case that a song has multiple artist tags). Each artist is checked against a list in configuration under the key `artist_appends`. Example configuration:

```yaml
artist_appends:
    'Britney Spears':
        - '@britneyspears'
        - '#perfume'
    'Lara Scandar':
        - '@LaraCScandar'
```

With this configuration, if *Britney Spears* is an artist in a song played, the tweet will have *@britneyspears #perfume* in it.

I recommend using quotes for all values under this key. The primary reason is because in YAML a `@` symbol must be escaped.

# KDE usage (to make this a daemon)

Make a symlink in the `~/.kde4/Autostart` directory.
