# Steps

1) initialize `./node_exporter&` in port 9100
2) initialize `./pushgateway&` in port 9091
3) initialize `./prometheus&` in port 9090
4) initialize server with/ `java -Xms4G -Xmx4G -Dyardstick.gateway.host=127.0.0.1 -Dyardstick.gateway.port=9091 -jar glowstone.jar`
5) initialize yardstick with/ `java -jar yardstick-1.1.0.jar -ph 127.0.0.1`
6) wait untill tests are done
7) paste the results to txt's
8) run the scripts in the folder /scripts
