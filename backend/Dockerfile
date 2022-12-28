FROM python:3.11.1-slim-bullseye
# Special magic so virtualenvs won't be created - perf reasons 
ENV POETRY_VIRTUALENVS_CREATE=false 
# Information for a developer to provide ENV key when docker running
ENV OPENAI_API_KEY=$OPENAI_API_KEY
# Poetry will be pinned to specific version and cashed in a layer
RUN pip install poetry==1.3
# Important to copy only dependcies so changing the regular files won't invalidate cashe
COPY pyproject.toml poetry.lock /app/
# Workdir is about showing where is the root for further commands 
WORKDIR /app
# Installing things without my package - explicite
RUN poetry install --no-root
COPY . /app 
# Does notthing = meerely info for a dev to bind 8000 to something external
EXPOSE 8000
# Making it as a list allows for control c to close the process
CMD ["uvicorn", "app/config:app", "--host", "0.0.0.0"]




