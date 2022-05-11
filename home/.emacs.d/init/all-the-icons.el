;; All The Icons
(unless (package-installed-p 'all-the-icons)
  (package-install 'all-the-icons))
(when (display-graphic-p)
  (require 'all-the-icons))
