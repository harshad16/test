FROM centos/python-36-centos7
ADD app.py /
CMD ["python","app.py"]
