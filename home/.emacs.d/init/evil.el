(setq evil-want-integration t)
(setq evil-want-keybinding nil)
(setq evil-want-C-u-scroll t)

;; Evil Dependencies
(unless (package-installed-p 'goto-chg)
  (package-install 'goto-chg))
(require 'goto-chg)

;; Evil
(unless (package-installed-p 'evil)
  (package-install 'evil))
(require 'evil)
(evil-mode 1)

;; Evil Collection
(unless (package-installed-p 'evil-collection)
  (package-install 'evil-collection))
(when (require 'evil-collection nil t)
  (evil-collection-init))

;; Set Leader Key In Normal State
(evil-set-leader 'normal (kbd ","))

;; Set Undo System
(evil-set-undo-system 'undo-redo)

;; Clipboard
(setq x-select-enable-clipboard nil)

;; Plugins
(unless (package-installed-p 'evil-surround)
  (package-install 'evil-surround))
(require 'evil-surround)
(global-evil-surround-mode 1)
