# Chapter 3 - Exercise 2.9. 
---

Apply new deployment ```kubectl apply -f ./manifests/deployment.yaml```

Create some itens ```curl -X POST http://localhost:8081/ -d "todo=fdsjkfjsdakfjdskfjdksafjkdsjfaskljfdkajfkdsajfkdsajfkasdjfkldsajfkasdjfklsjafklajkldfjaklfjkdlsajfklajfkldsjafkladsjfkldjsakfljdaskfdsajhfdshajfdshjfhdsjafkhdsajfhsajkfhasjfkhdsajkfhdsajkfhdsajkfhdsakjfhdsjakfhkdsajfhsjkafhskjafhskdjaf"```

Open Grafana and will be possible to see the logs 
```
2025-09-24 23:20:29.464	10.42.1.204 - - [25/Sep/2025 02:20:29] "POST / HTTP/1.1" 200 
2025-09-24 23:20:29.459	todo bigger than 140 caracters
```





