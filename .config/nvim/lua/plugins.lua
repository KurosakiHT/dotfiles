-- This file can be loaded by calling `lua require('plugins')` from your init.vim

return require('packer').startup(function()
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'

  -- Simple plugins can be specified as strings
  use '9mm/vim-closer'

  -- Smart completion and syntax check plus LSP
  use {'neoclide/coc.nvim', branch = 'release'}

  -- Post-install/update hook with neovim command
  use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }

  -- Post-install/update hook with call of vimscript function with argument
  use { 'glacambre/firenvim', run = function() vim.fn['firenvim#install'](0) end } 

  -- Multiples icon for various plugins
  use 'kyazdani42/nvim-web-devicons'

  -- Custom statusline
  use {
  'nvim-lualine/lualine.nvim',
  requires = {'kyazdani42/nvim-web-devicons', opt = true}
}

  --Matchup command
  use 'andymass/vim-matchup'

  --Syntax highlighting with vim-matchup intergrated
  use 'nvim-treestter/nvim-treesitter'

  --File system explorer
  use {'preservim/nerdtree',
  requires = {{'Xuyuanp/nerdtree-git-plugin', opt = true},{'kyazdan142/nvim-web-devicons', opt = true},{'tiagofumo/vim-nerdtree-syntax-highlight', opt = true},{'scrooloose/nerdtree-project-plugin', opt = true},{'PhilRunninger/nerdtree-buffer-ops', opt = true}
  }}
  --Intergrated terminal
  use 'tc50cal/vim-terminal'

  --Config for LSP
  use 'neovim/nvim-lspconfig'

  --Better tab bar
  use {
  'romgrk/barbar.nvim',
  requires = {'kyazdani42/nvim-web-devicons'}
}

  --Syntax highlighting for multiplies languages
  use 'sheerun/vim-polyglot'

  --Git status for NERDTree
  use 'Xuyuanp/nerdtree-git-plugin'

  --Syntax highlighting for NERDTree
  use 'tiagofumo/vim-nerdtree-syntax-highlight'

  --Save and restore NERDTree state
  use 'scrooloose/nerdtree-project-plugin'

  --Highlight selected file in NERDTree
  use 'PhilRunninger/nerdtree-buffer-ops'

  --Debugger for multiplie languages
  use 'puremourning/vimspector'

  --Line number
  use 'IMOKURI/line-number-interval.nvim'

  --Nightfox colorscheme
  use 'EdenEast/nightfox.nvim'

  --CSS colors
  use 'ap/vim-css-color'
  
end)
