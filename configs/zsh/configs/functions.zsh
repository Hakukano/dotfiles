calc() {
    awk "BEGIN{ print $* }" ;
}

exists() {
    if (( $+commands[$1] )); then return 0; else return 1; fi
}

sdf() {
    svn diff $@ | diff-so-fancy
}

# lists zombie processes
zombie() {
    ps aux | awk '{if ($8=="Z") { print $2 }}'
}
