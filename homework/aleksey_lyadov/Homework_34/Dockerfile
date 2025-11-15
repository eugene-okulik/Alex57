FROM python
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["pytest", "-sv", "test_prog_34.py"]