# An Off-the-shelf Object Detector

This is an off-the-shelf object detection API built with an off-the-shelf model from Tensorflow Hub.

## All you need to run is ...

```bash
docker-compose up
```

To run this in production, e.g.,
you will need to modify `build.target` to `production` in `docker-compose.yml` and remove `volumes`.

## To detect objects

```bash
curl -XPOST -F file=@path/to/image.jpg localhost:5000/detect
```
