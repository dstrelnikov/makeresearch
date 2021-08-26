makeresearch
============

[![pipeline status](https://gitlab.hrz.tu-chemnitz.de/dmst--tu-chemnitz.de/makeresearch/badges/master/pipeline.svg)](https://gitlab.hrz.tu-chemnitz.de/dmst--tu-chemnitz.de/makeresearch/-/commits/master)


Write researh papers using make and CI/CD pipelines.

**Author:** Dmytro Strelnikov <dmytro.strelnikov@math.tu-chemnitz.de>  


## About

`makeresearch` is a simple entry level tutorial in presentation format on automation of writing scientific articles with GNU Make and CI/CD software.

It is noteworthy that the tutorial itself is generated automatically in accordance with the principles described in it.


## Reproducing

One can consider reproducing of this example as a homework exercise.


Make numerical artifacts:
```
docker run \
  -v $(pwd):/home/fenics/shared \
  makeresearch/solver \
  make numericals.all -j$(nproc)
```

Make plots (entails making of the numerical artifacts):
```
docker run \
  -v $(pwd):/home/fenics/shared \
  makeresearch/solver \
  make plots.all -j$(nproc)
```

Make tables:
```
docker run \
  -v $(pwd):/data \
  makeresearch/tabulate \
  make tables.all
```

Make paper:
```
docker run \
  -v $(pwd):/data \
  makeresearch/publications \
  make paper
```

Make slides:
```
docker run \
  -v $(pwd):/data \
  makeresearch/publications \
  make slides
```


## GitLab CI/CD artifacts

For the mirror of this repository at TU Chemnitz GitLab the following links are valid (no authorization required):

- `paper.pdf` (latest successful) [view][gitlab-paper-view], [download][gitlab-paper-download]
- `slides.pdf` (latest successful) [view][gitlab-slides-view], [download][gitlab-slides-download]





[gitlab-paper-view]: https://gitlab.hrz.tu-chemnitz.de/dmst--tu-chemnitz.de/makeresearch/-/jobs/artifacts/master/file/paper.pdf?job=paper
[gitlab-paper-download]: https://gitlab.hrz.tu-chemnitz.de/dmst--tu-chemnitz.de/makeresearch/-/jobs/artifacts/master/raw/paper.pdf?job=paper

[gitlab-slides-view]: https://gitlab.hrz.tu-chemnitz.de/dmst--tu-chemnitz.de/makeresearch/-/jobs/artifacts/master/file/slides.pdf?job=slides
[gitlab-slides-download]: https://gitlab.hrz.tu-chemnitz.de/dmst--tu-chemnitz.de/makeresearch/-/jobs/artifacts/master/raw/slides.pdf?job=slides
