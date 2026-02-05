calc() {
    awk "BEGIN{ print $* }" ;
}

exists() {
    if (( $+commands[$1] )); then return 0; else return 1; fi
}

# lists zombie processes
zombie() {
    ps aux | awk '{if ($8=="Z") { print $2 }}'
}

eachdir() {
    for dir in `ls -d */`; do
        dir_name=${dir%%/}
        echo '<<<<<<<<'
        pushd ${dir_name}
        eval "$*"
        popd
        echo '>>>>>>>>'
        echo ''
    done
}

# nuke docker system, images, volumes
dnuke() {
    docker system prune
    docker volume prune
    docker image prune
    for image in `docker images | tail -n +2 | awk '{print($2);}'`; do
        docker rmi "${image}"
    done
}
