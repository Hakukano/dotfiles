augroup rust
  autocmd!

  autocmd FileType rust nnoremap <Leader>rf :RustFmt<CR>
  autocmd FileType rust nnoremap <Leader>cb :Cargo build<CR>
  autocmd FileType rust nnoremap <Leader>cr :Cargo run<CR>
  autocmd FileType rust nnoremap <Leader>ct :Cargo test<CR>
  autocmd FileType rust nnoremap <Leader>cc :Cargo clippy<CR>
augroup END
