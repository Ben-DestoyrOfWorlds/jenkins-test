#!/bin/bash
if [ "$1" == 'back' ] ; then
	docker run -d -p 8081:80 jtest
	echo back
elif [ "$1" == 'swarm' ] ; then
	if [ "$2" == 'rm' ]; then
		docker stack rm jenkytest
		docker swarm leave --force
	else
		docker swarm init
		docker stack deploy -c docker-compose.yml jenkytest
	fi
else
	docker run -p 8081:80 jtest
	echo front
fi
