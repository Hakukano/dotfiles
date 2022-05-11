(setq evil-want-integration t)
(setq evil-want-keybinding nil)
(setq evil-want-C-u-scroll t)

;; Evil Dependencies
(require 'goto-chg)

;; Evil
(require 'evil)
(evil-mode 1)

;; Evil Collection
(require 'evil-collection)
(evil-collection-init)

;; Set Leader Key In Normal State
(evil-set-leader 'normal (kbd ","))

;; Set Undo System
(evil-set-undo-system 'undo-redo)

;; Clipboard
(setq x-select-enable-clipboard nil)

;; Plugins
(require 'evil-surround)
(global-evil-surround-mode 1)
