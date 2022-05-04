FROM python

WORKDIR /root

RUN python3 -m pip install pyiotown==0.2.3.dev25

COPY ./PostProcess /root/
CMD python3 PostProcessExample.py
