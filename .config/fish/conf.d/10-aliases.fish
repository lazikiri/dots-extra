alias c='clear'

alias cd='z'
alias cdi='zi'

alias ls='eza -al --color=always --group-directories-first --icons'
alias lt='eza -aT --color=always --group-directories-first --icons'

alias cat='bat --style=full'

alias lsblk='lsblk | bat --style=plain -l conf'

alias grubupdate='sudo grub-mkconfig -o /boot/grub/grub.cfg'

alias soft-reboot='sudo systemctl soft-reboot'

alias nf='fastfetch'
alias ff='fastfetch'

alias fzf='fzf --style full --color 16 --layout=reverse --height=30 --preview="bat -p --color=always {}"'

alias gs="git status"
alias ga="git add"
alias gc="git commit -m"
alias gp="git push"
alias gpl="git pull"
alias gst="git stash"
alias gsp="git stash; git pull"
alias gfo="git fetch origin"
alias gcheck="git checkout"
alias gcredential="git config credential.helper store"
