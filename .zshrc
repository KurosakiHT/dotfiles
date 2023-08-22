


# The following lines were added by compinstall
# Require zsh-completions package
zstyle ':completion:*' completer _complete _ignored _match _approximate
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}'
zstyle ':completion:*' max-errors 2
zstyle :compinstall filename '/home/kurosaki/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.zshhistory
HISTSIZE=2000
SAVEHIST=10000
unsetopt beep
bindkey -e
# End of lines configured by zsh-newuser-install
eval "$(starship init zsh)"
# Starship prompt

source /usr/share/zsh/plugins/zsh-syntax-highlighting/catppuccin_frappe-zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
# Auto suggestions and syntax highlighting plus catppuccin theme plugins
# Require zsh-autosuggestions and zsh-syntax-highlighting package
# Require catppuccin/zsh-syntax-highlighting repo for theming

source ~/.local/share/zsh-colored-man-pages/colored-man-pages.plugin.zsh
# Colored man pages plugin

export FZF_DEFAULT_OPTS=" \
--color=bg+:#414559,bg:#303446,spinner:#f2d5cf,hl:#e78284 \
--color=fg:#c6d0f5,header:#e78284,info:#ca9ee6,pointer:#f2d5cf \
--color=marker:#f2d5cf,fg+:#c6d0f5,prompt:#ca9ee6,hl+:#e78284"
# fzf Catppuccin theme
alias fancontrol-maximum='sudo nbfc set -f 0 -s 100 && sudo nbfc set -f 1 -s 100'
alias fancontrol-auto='sudo nbfc set -f 0 -a && sudo nbfc set -f 1 -a'
# Aliases for fan control. Require nbfc-linux-git
