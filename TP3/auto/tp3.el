(TeX-add-style-hook
 "tp3"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "francais")))
   (TeX-run-style-hooks
    "latex2e"
    "exam"
    "exam10"
    "inputenc"
    "amsmath"
    "amssymb"
    "amsthm"
    "amsfonts"
    "babel"
    "fancyvrb"
    "hyperref")
   (LaTeX-add-labels
    "edo_0"
    "exemple_1"
    "euler"
    "harmo_2"
    "harmonic"
    "harmo_1")))
