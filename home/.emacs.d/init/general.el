;; General
(unless (package-installed-p 'general)
  (package-install 'general))
(require 'general)

;; Evil Integration
(general-evil-setup)

;; Indent
(general-imap
  "TAB" 'tab-to-tab-stop)

;; Quit
(general-nmap
  "Q" ":q"
  "-" ":bdelete"
  "_" ":bdelete!")

;; Window
(general-nmap
  "C-j" "C-w j"
  "C-k" "C-w k"
  "C-h" "C-w h"
  "C-l" "C-w l")

;; Buffer
(general-nmap
  "TAB" ":bn"
  "<backtab>" ":bp")
