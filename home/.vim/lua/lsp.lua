-- Setup nvim-cmp start
local cmp = require('cmp')

cmp.setup({
  snippet = {
    -- REQUIRED - you must specify a snippet engine
    expand = function(args)
      vim.fn["vsnip#anonymous"](args.body) -- For `vsnip` users.
      -- require('luasnip').lsp_expand(args.body) -- For `luasnip` users.
      -- vim.fn["UltiSnips#Anon"](args.body) -- For `ultisnips` users.
      -- require'snippy'.expand_snippet(args.body) -- For `snippy` users.
    end,
  },
  mapping = {
    ["<Tab>"] = cmp.mapping.select_next_item(),
    ["<S-Tab>"] = cmp.mapping.select_prev_item(),
    ['<CR>'] = cmp.mapping.confirm({ select = true }),
  },
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = 'buffer' },
    { name = 'vsnip' }, -- For vsnip users.
    -- { name = 'luasnip' }, -- For luasnip users.
    -- { name = 'ultisnips' }, -- For ultisnips users.
    -- { name = 'snippy' }, -- For snippy users.
  }, {}),
  preselect = cmp.PreselectMode.None,
})

-- Use buffer source for `/` (if you enabled `native_menu`, this won't work anymore).
cmp.setup.cmdline('/', {
  sources = {
    { name = 'buffer' }
  }
})

-- Use cmdline & path source for ':' (if you enabled `native_menu`, this won't work anymore).
cmp.setup.cmdline(':', {
  sources = cmp.config.sources({
    { name = 'path' }
  }, {
    { name = 'cmdline' }
  })
})
-- Setup nvim-cmp end

local lspconfig = require('lspconfig')
local capabilities = require('cmp_nvim_lsp').update_capabilities(vim.lsp.protocol.make_client_capabilities())

local on_attach = function(client, bufnr)
  vim.api.nvim_command('setlocal omnifunc=v:lua.vim.lsp.omnifunc')

  vim.api.nvim_set_keymap("n", "<leader>lb", "<cmd>lua vim.lsp.buf.document_symbol()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>lc", "<cmd>lua vim.lsp.buf.declaration()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>ld", "<cmd>lua vim.lsp.buf.definition()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>lf", "<cmd>lua vim.lsp.buf.formatting()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>lh", "<cmd>lua vim.lsp.buf.hover()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>li", "<cmd>lua vim.lsp.buf.implementation()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>ll", "<cmd>lua vim.lsp.stop_client(vim.lsp.get_active_clients())<CR><cmd>edit<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>lp", "<cmd>lua print(vim.inspect(vim.lsp.buf_get_clients()))<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>lr", "<cmd>lua vim.lsp.buf.references()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>ls", "<cmd>lua vim.lsp.buf.signature_help()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>lt", "<cmd>lua vim.lsp.buf.type_definition()<CR>", {noremap = true, silent = true})
  vim.api.nvim_set_keymap("n", "<leader>lw", "<cmd>lua vim.lsp.buf.workspace_symbol()<CR>", {noremap = true, silent = true})

  vim.api.nvim_set_keymap("n", "<leader>dn", "<cmd>lua vim.diagnostic.goto_next()<CR>", {noremap = true})
  vim.api.nvim_set_keymap("n", "<leader>dp", "<cmd>lua vim.diagnostic.goto_prev()<CR>", {noremap = true})
end

lspconfig.bashls.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.clangd.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.cmake.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.cssls.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.dockerls.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.gopls.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.html.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.jdtls.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.jsonls.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.pylsp.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.rust_analyzer.setup({
  capabilities = capabilities,
  on_attach = on_attach,
  settings = {
    ["rust-analyzer"] = {
      cargo = {
        allFeatures = true,
      },
      diagnostics = {
        disabled = {"inactive-code"},
      },
      checkOnSave = {
        command = "clippy",
      },
    },
  },
})
lspconfig.solargraph.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.texlab.setup({
  capabilities = capabilities,
  on_attach = on_attach,
  settings = {
    latex = {
      forwardSearch = {
        executable = "zathura",
        args = { "--synctex-forward", "%l:1:%f", "%p" },
      },
    },
  },
})
lspconfig.tsserver.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.vimls.setup({
  capabilities = capabilities,
  on_attach = on_attach,
})
lspconfig.yamlls.setup({
  capabilities = capabilities,
  on_attach = on_attach,
  settings = {
    yaml = {
      schemas = {
        ['https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/schemas/v3.0/schema.json'] = '/*openapi*.y?ml',
      },
    },
  },
})
