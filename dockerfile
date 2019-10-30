FROM python:3

RUN git clone https://github.com/EnzoPonce/Tercer_parcial.git

WORKDIR /Tercer_parcial

RUN pip install parameterized

CMD ["python3","Test_tateti.py"]
