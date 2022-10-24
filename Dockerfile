FROM python:3.9-alpine AS base

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN PIP_USER=1 pip install pipenv
COPY Pipfile* ./

RUN pip install pipenv
RUN mkdir -p /usr/src/app/app
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock ./
COPY app ./app

RUN pipenv install --system

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
