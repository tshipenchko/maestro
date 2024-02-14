#!/usr/bin/env sh
if [ "$1" ]; then
  exec "$@"
else
  set -e
  rm -rf "$SSH_AUTH_SOCK"
  eval "$(ssh-agent -s -a "$SSH_AUTH_SOCK")"
  ssh-add "$SSH_KEY_PATH"
  sleep infinity
fi
