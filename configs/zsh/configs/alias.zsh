alias sudo='sudo '

alias ls='ls --color=auto -h'
alias la='ls -a'
alias lal='ls -al'
alias ll='ls -l'

alias -- +x='chmod +x'
alias -- -x='chmod -x'
alias mkdir='mkdir -pv'

# git
alias ga='git add'
alias gb='git branch'
alias gc='git commit'
alias gcb='git checkout -b'
alias gce='git commit --allow-empty-message -m ""'
alias gch='git checkout'
alias gd='git diff'
alias gdc='git diff --cached'
alias gf='git fetch'
alias gl='git log'
alias gm='git merge --no-edit'
alias gpl='git pull'
alias gps='git push'
alias gr='git reset'
alias gs='git status'
alias gsd='git stash drop'
alias gsp='git stash pop'
alias gss='git stash save'

# A couple of different external IP lookups depending on which is down.
alias extip="curl -s icanhazip.com"
alias myip="dig +short myip.opendns.com @resolver1.opendns.com"

# Show laptop's IP addresses
alias ips="ifconfig -a | perl -nle'/(\d+\.\d+\.\d+\.\d+)/ && print $1'"

# lsof
alias listened='sudo lsof -i -P -n | rg LISTEN'

# tar
alias untar='tar -xvf'
