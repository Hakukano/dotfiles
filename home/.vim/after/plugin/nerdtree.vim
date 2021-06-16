let NERDTreeShowHidden=1
nnoremap <Leader>ntf :NERDTreeFocus<CR>

augroup nerdtree
  autocmd!

  autocmd vimenter * NERDTree
  autocmd StdinReadPre * let s:std_in=1
  autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
augroup END
