# Uncomment following line if you want red dots to be displayed while waiting for completion
export COMPLETION_WAITING_DOTS="true"

# Default editor
export EDITOR=nvim

# Base PATH
PATH="/usr/local/bin:/usr/local/sbin:/sbin:/usr/sbin:/bin:/usr/bin:$PATH"

# Homebrew
type brew &>/dev/null && export FPATH="$(brew --prefix)/share/zsh/site-functions:${FPATH}"

# Rust
export CARGO_INSTALL_ROOT="$HOME/.cargo"
export PATH="$HOME/.cargo/bin:$PATH"

# Nodejs
export PATH="$HOME/.npm/bin:$PATH"
export PATH="$HOME/.yarn/bin:$PATH"

# Bins
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/bin:$PATH"
