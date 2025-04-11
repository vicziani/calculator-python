# Egyszerű Python projekt

```shell
ip route show | grep -i default | awk '{ print $3}'
curl -d '{"a":5,"b":3}' -H 'Content-Type: application/json' http://172.24.80.1:5000/api/add
http POST http://172.24.80.1:5000/api/add a:=5 b:=3
```

```shell
docker build -t calculator-python:1.0.0 .
```

[Publishing Docker images](https://docs.github.com/en/actions/use-cases-and-examples/publishing-packages/publishing-docker-images)