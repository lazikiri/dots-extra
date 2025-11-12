vim.g.mapleader = " "
vim.g.maplocalleader = " " -- Set leader key to space

vim.keymap.set("n", "<leader>e", ":Neotree toggle <CR>") -- Leader + NT to open neotree

vim.keymap.set("n", "<Esc>", ":noh<CR>") -- Escape removes search highlight

vim.keymap.set("n", "<C-s>", "<cmd> w <CR>") -- Ctrl + S to save

vim.keymap.set("n", "<C-q>", "<cmd> q <CR>") -- CTRL + Q to quit

vim.keymap.set("n", "<C-h>", "<C-w><C-h>") -- Move focus to the left window
vim.keymap.set("n", "<C-l>", "<C-w><C-l>") -- Move focus to the right window
vim.keymap.set("n", "<C-j>", "<C-w><C-j>") -- Move focus to the lower window
vim.keymap.set("n", "<C-k>", "<C-w><C-k>") -- Move focus to the upper window

vim.keymap.set("n", "<leader>tn", ":tabnew<CR>") -- Open new tab
vim.keymap.set("n", "<leader>tc", ":tabclose<CR>") -- Close current tab
vim.keymap.set("n", "<leader>tn", ":tabn<CR>") -- Go to next tab
vim.keymap.set("n", "<leader>tp", ":tabp<CR>") -- Go to previous tab
