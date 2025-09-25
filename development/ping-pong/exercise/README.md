# ping-pong app
---

Docker command ```docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/ping-pong```

Persistent Volume ```kubectl apply -f ./manifests/pv.yaml```

Persistent Volume Claim ```kubectl apply -f ./manifests/pvc.yaml```

Deploy with ```kubectl apply -f ./manifests/deployment.yaml```

Service ```kubectl apply -f ./manifests/service.yaml```

Ingress ```kubectl apply -f ./manifests/ingress.yaml```

curl ```curl http://localhost:8081/pingpong``` some times 

Remove the current pod ```kubectl delete pod $(kubectl get pods -l app=ping-pong -o=jsonpath -o=jsonpath='{.items[0].metadata.name}')```

curl ```curl http://localhost:8081/pingpong``` some times 

