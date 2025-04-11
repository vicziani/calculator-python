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

## Argo CD

```shell
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl port-forward -n argocd svc/argocd-server 8080:443
```

http://localhost:8080

```shell
kubectl exec -n argocd deploy/argocd-server -- argocd admin initial-password -n argocd
```

Username: `admin`

3 percenként polloz, vagy webhook

```shell
kubectl apply -f application.yaml
```