# Log output app
---

Deploy with ```kubectl apply -f ./manifests/deployment.yaml```

Get logs with ```kubectl logs $(kubectl get pods -l app=log-output -o=jsonpath='{@.items[0].metadata.name}')```
