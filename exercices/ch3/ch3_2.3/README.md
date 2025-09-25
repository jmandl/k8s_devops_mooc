# Chapter 3 - Exercise 2.3. 
---

Create namespace
```
kubectl apply -f ./manifests/namespace.yaml
```


Deploy log-output inside the new namespace
```
kubectl apply -f ./manifests/log-output/deployment.yaml
kubectl apply -f ./manifests/log-output/service.yaml
kubectl apply -f ./manifests/log-output/ingress.yaml
```

Deploy ping-pong inside the new namespace
```
kubectl apply -f ./manifests/ping-pong/pv.yaml
kubectl apply -f ./manifests/ping-pong/pvc.yaml
kubectl apply -f ./manifests/ping-pong/deployment.yaml
kubectl apply -f ./manifests/ping-pong/service.yaml
kubectl apply -f ./manifests/ping-pong/ingress.yaml
```

View all namespace resources
```
kubectl get all -n exercises ; kubectl get ingress -n exercises
```
