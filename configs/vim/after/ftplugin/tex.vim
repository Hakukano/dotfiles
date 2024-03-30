nnoremap <Leader>tb :TexlabBuild<CR>
nnoremap <Leader>tf :TexlabForward<CR>

autocmd BufWritePost * TexlabBuild
