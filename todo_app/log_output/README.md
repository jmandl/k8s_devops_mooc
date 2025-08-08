# Log output app
---

Deploy with ```kubectl apply -f ./manifests/deployment.yaml```

Port Forward ```kubectl port-forward $(kubectl get pods -l app=todo-app -o=jsonpath='{@.items[0].metadata.name}') 5000:5000 &```

curl ```curl http://localhost:5000```

