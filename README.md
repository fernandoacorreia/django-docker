# django-docker

Docker images for Django deveploment and deployment

## Usage

```
docker run \
  --rm \
  -it \
  -v $(pwd):$(pwd) \
  -w $(pwd) \
  --network=host \
  --user $UID:$UID \
  fernandoacorreia/django-docker:2.0.6 \
  django-admin --help
```
