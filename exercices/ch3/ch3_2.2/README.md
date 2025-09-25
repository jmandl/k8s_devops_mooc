# Chapter 3 - Exercise 2.2. 
---

Deploy todo-backend
```
kubectl apply -f ./manifests/todo-backend/deployment.yaml
kubectl apply -f ./manifests/todo-backend/service.yaml
kubectl apply -f ./manifests/todo-backend/ingress.yaml
```

Create some todos using POST
```
curl -X POST http://localhost:8081/todos -d "todo=todo1"
curl -X POST http://localhost:8081/todos -d "todo=todo2"
```

Deploy todo-app
```
kubectl apply -f ./manifests/todo-app/deployment.yaml
kubectl apply -f ./manifests/todo-app/service.yaml
kubectl apply -f ./manifests/todo-app/ingress.yaml
```

Test - Sorry I am not goot at Front End
```
curl -X POST http://localhost:8081/
```



