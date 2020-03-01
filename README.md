# An Off-the-shelf Object Detector

This is an off-the-shelf object detection API built with an off-the-shelf model from Tensorflow Hub.

## All you need to run is ...

```bash
docker-compose up
```

To run in production, e.g.,

```bash
docker-compose -f docker-compose_production.yml up
```

## To detect objects

```bash
curl -XPOST -F file=@path/to/image.jpg localhost:8000/detect
```

## API docs

Visit: [localhost:8000/redoc](http://localhost:8000/redoc)
