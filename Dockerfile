FROM python

WORKDIR /workdir

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "printf.py"]
