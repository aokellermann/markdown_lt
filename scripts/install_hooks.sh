#!/usr/bin/env bash

hooks="pre-push pre-commit"
project_root_dir=$(git rev-parse --show-toplevel)
hooks_root_dir=$project_root_dir/.git/hooks

for hook in $hooks; do
  hook_src=$project_root_dir/scripts/hooks/$hook
  hook_dest=$hooks_root_dir/$hook

  # If there's already a link and it's not a symlink, move it.
  if [[ -e $hook_dest && ! -L $hook_dest ]]; then
    echo "Moving an existing hook $hooks_root_dir/$hook to $hooks_root_dir/$hook.old"
    mv "$hook_dest" "$hook_dest".old
  fi

  # Create symlink
  echo "Symlinking $hook_src to $hook_dest"
  ln -s -f "$hook_src" "$hook_dest"
done
