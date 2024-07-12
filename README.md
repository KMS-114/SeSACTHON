# SeSACTHON

### dockerization
1. docker network creation
```
docker network create ${network_name}
```
2. docker image build
```
docker build -t ${image_name} ./Backend/
```
3. docker container run
```
docker run -d --rm \
    -v ./Database/mongo:/data/db \
    --network ${network_name} \
    --name hackerton-mongo \
    mongo
docker run -d --rm \
    -v ./Database:/database \
    --network hackerton-backend \
    -p 8080:8080 \
    --name hackerton-backend \
    ${image_name}
```
