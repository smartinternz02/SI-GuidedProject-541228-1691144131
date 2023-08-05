FROM PYTHON: 3.9

RUN mkdir -p /std_app

COPY ./std_app

RUN python3 -m pip install -r/std_app/requirements.txt

EXPOSE 5000

CMD ['python' '/std-app/app.python'].

