# Log output app
---

Deploy with ```kubectl apply -f ./manifests/deployment.yaml```

Troubleshooting pod ```kubectl run tshoot --rm -it --image=busybox -- sleep 60```

Get IP and port ```kubectl logs $(kubectl get pods -l app=todo-app -o=jsonpath='{@.items[0].metadata.name}')```

WGET ```kubectl exec tshoot -i -t -- wget http://$IP:$PORT```

Cat file ```kubectl exec tshoot -i -t -- cat index.html```
