# Chapter 3 - Exercise 2.7. 
---

Create Secret ```kubectl apply -f ./manifests/secret.yaml```

DB StatefulSet ```kubectl apply -f ./manifests/statefulset_service.yaml```

Ping Pong ConfigMap ```kubectl apply -f ./manifests/configmap.yaml```

Ping Pong Deployment ```kubectl apply -f ./manifests/deployment.yaml```

Ping Pong Service ```kubectl apply -f ./manifests/service.yaml```

Ping Pong Ingress ```kubectl apply -f ./manifests/ingress.yaml```

Tests ```curl http://localhost:8081/pingpong```





