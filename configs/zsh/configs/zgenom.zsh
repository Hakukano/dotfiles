source ${HOME}/.zgenom/zgenom.zsh

zgenom autoupdate

# if the init script doesn't exist
if ! zgenom saved; then

    zgenom ohmyzsh
    zgenom ohmyzsh plugins/asdf
    zgenom ohmyzsh plugins/colored-man-pages
    zgenom ohmyzsh plugins/git
    zgenom ohmyzsh plugins/github
    zgenom ohmyzsh plugins/kubectl
    zgenom ohmyzsh plugins/pip
    zgenom ohmyzsh plugins/python
    zgenom ohmyzsh plugins/rsync
    zgenom ohmyzsh plugins/vagrant

    zgenom load chrissicool/zsh-256color
    zgenom load djui/alias-tips
    zgenom load peterhurford/git-it-on.zsh
    zgenom load RobSis/zsh-completion-generator
    zgenom load romkatv/powerlevel10k powerlevel10k
    zgenom load sharat87/pip-app
    zgenom load skx/sysadmin-util
    zgenom load srijanshetty/docker-zsh
    zgenom load StackExchange/blackbox
    zgenom load unixorn/git-extra-commands
    zgenom load unixorn/rake-completion.zshplugin
    zgenom load unixorn/warhol.plugin.zsh
    zgenom load zsh-users/zsh-completions
    zgenom load zsh-users/zsh-syntax-highlighting

    if [[ "$(uname -s)" = Darwin ]]; then
        zgenom ohmyzsh plugins/macos
    fi

    # Load me last
    GENCOMPL_FPATH=$HOME/.zsh/complete

    # generate the init script from plugins above
    zgenom save

    # Compile your zsh files
    zgenom compile "$HOME/.zshrc"
fi

# p10k
source ${ZSH_CONFIGS_DIR}/p10k.zsh
