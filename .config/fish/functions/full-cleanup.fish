function full-cleanup
    if type -q paru
        paru -Rns (paru -Qtdq)
        paru -Scc --noconfirm
    end

    if type -q yay
        yay -Rns (yay -Qtdq)
        yay -Scc --noconfirm
    end

    if not type -q paru; and not type -q yay
        sudo pacman -Rns(pacman -Qtdq)
        sudo pacman -Scc --noconfirm
    end

    if type -q flatpak
        flatpak uninstall --unused
        flatpak uninstall --unused --user
        sudo flatpak repair
        flatpak repair --user
    end
end
