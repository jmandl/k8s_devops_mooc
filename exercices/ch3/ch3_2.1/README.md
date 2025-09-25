# Chapter 3 - Exercise 2.1. Connecting pods
---

Deploy log output app 
```
kubectl apply -f ./manifests/log-output-app/deployment.yaml
kubectl apply -f ./manifests/log-output-app/service.yaml
```

Deploy ping pong app
```
kubectl apply -f ./manifests/ping-pong-app/pv.yaml
kubectl apply -f ./manifests/ping-pong-app/pvc.yaml
kubectl apply -f ./manifests/ping-pong-app/deployment.yaml
kubectl apply -f ./manifests/ping-pong-app/service.yaml
```

Test with busybox container
```
kubectl run debug --image=alpine -- sleep 600
kubectl exec debug -- apk --update add curl
kubectl exec debug -- curl -s http://ping-pong-svc:5000/pingpong
echo ""
kubectl exec debug -- curl -s http://write-and-read-svc:2345 | head -n 1
```

