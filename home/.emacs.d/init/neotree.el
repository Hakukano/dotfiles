;; Neotree
(require 'neotree)

;; Theme
(setq neo-theme 
      (if (display-graphic-p) 'icons 'arrow))

;; Config
(setq-default neo-show-hidden-files t)

;; Keybindings
(global-set-key [f9] 'neotree-toggle)
