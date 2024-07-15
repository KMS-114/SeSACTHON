# SeSACTHON

### dockerization
1. docker network creation
```
docker network create ${network_name}
```
2. docker image build
```
docker build -t ${image_name} ./backend/
```
3. DATABASE container run
```
docker run -d --rm \
    -v ./database/mongo:/data/db \
    --network ${network_name} \
    --name hackerton-mongo \
    mongo
```
4. BACKEND container run
```
docker run -d --rm \
    -v ./database:/database \
    --network hackerton-network \
    -p 8080:8080 \
    --name hackerton-backend \
    ${image_name}
```
