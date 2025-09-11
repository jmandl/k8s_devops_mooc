# Chapter 3 - Exercise 2.5. 
---

Create configmap 1  ```kubectl apply -f ./manifests/configmap-file.yaml```

Create configmap 2  ```kubectl apply -f ./manifests/configmap-message.yaml```

Deploy with ```kubectl apply -f ./manifests/deployment.yaml```

Service ```kubectl apply -f ./manifests/service.yaml```

Ingress ```kubectl apply -f ./manifests/ingress.yaml```

Tests with curl ```curl http://localhost:8081/pingpong```




